# 这个文件是用来存储数据库中得到信息的中转用的
from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
import requests
import json

PATH = '127.0.0.1:5000'  # '139.59.115.34:5000'


class log_data():
    """
    登录注册部分可能会用到的信息
    """

    def __init__(self, username='', password='', role='', test=False):
        self.identification = '管理员'
        self.verification = True  # 是否得到内容
        self.identify = True  # 密码是否正确
        self.room_id = 101
        self.token ,self.room_id= self.login(username, password, role, test)

    def login(self, username, password, role, test):
        #print(username, password, role)
        test_data = {
            'username': '222',
            'password': '222',
            'role': '管理员'
        }  # 测试用
        if test:
            data = test_data
        else:
            data = {
                'username': str(username),
                'password': str(password),
                'role': role
            }
        #print(data)
        response = requests.post(f'http://{PATH}/login',
                                 json=data
                                 )

        token = json.loads(response.content)['token']
        manager_token = json.loads(requests.post(f'http://{PATH}/login',
                                                 json=test_data).content)['token']
        headers = {
            'Authorization': 'Bearer ' + manager_token
        }
        response = requests.get(f'http://{PATH}/view-accounts', headers=headers)
        lst = json.loads(response.content)
        room_id=None
        for dict in lst:
            #print(dict)
            #print(data)
            #print(dict['username'] == data['username'] , dict['role'] == data['role'] , dict['roomNumber'] != None)
            if dict['username'] == data['username'] and dict['role'] == data['role'] and dict['roomNumber'] != None:
                #print('成功查找')
                room_id = dict['roomNumber']
        #print(lst)
        return token, room_id


class hotel_data():
    """
    酒店管理需要用到的信息
    """

    def __init__(self, username):
        self.room_id = None
        self.nused_id = None
        self.used_id = None
        self.username = username

    def __str__(self) -> str:
        return self.username

    def update_ac(self, room_id, input, token):
        headers = {
            'Authorization': 'Bearer ' + token
        }
        #print(token)
        response = requests.get(f'http://{PATH}/room-status/{int(room_id)}', headers=headers)
        data = json.loads(response.content)
        data['temperature'] = data['acTemperature']
        for key, value in input.items():
            if (key == 'switch'):
                if (value == 'true'):
                    if(data['isOn'] == 0):
                        data['isOn'] = 1
                    elif(data['isOn'] == 1):
                        data['isOn'] = 0
                    else:
                        data['isOn'] = not data['isOn']
            else:
                data[key] = value
        #print(data)
        response = requests.post(f'http://{PATH}//update-status/{int(room_id)}', json=data, headers=headers)
        #print(response.status_code)
        if (response.status_code == 200):
            print('更新成功')

    def room(self, token):
        """
        获取当前房屋的使用信息
        """
        # dahuangggg
        # response = requests.get('http://se.dahuangggg.me:8000/api/acounts/get_rooms_name/')
        # self.room_id = list(json.loads(response.content).values())[0] # 所有房间号
        # response = requests.get('http://se.dahuangggg.me:8000/api/conditioners/reception_get_room_number/')

        # self.nused_id = list(json.loads(response.content).values())[0] # 没人用的
        # print(self.nused_id)
        # self.nused_id = [key for key in self.nused_id.keys() if self.nused_id[key] == False]
        # self.used_id = [item for item in self.room_id if item not in self.nused_id]  # 有人在用

        headers = {
            'Authorization': 'Bearer ' + token
        }
        response = requests.get(f'http://{PATH}/rooms-available',
                                headers=headers
                                )
        # print(response.status_code)
        data = json.loads(response.content)
        print(data)
        self.room_id = [dict['number'] for dict in data]
        self.nused_id = [dict['number'] for dict in data if dict['occupied'] == False]
        self.used_id = [dict['number'] for dict in data if dict['occupied'] == True]
        return self.room_id, self.nused_id, self.used_id

    def check_in(self, user_name='', password='', idCard='', phone='', roomType='', days='', roomNumber='', token='',
                 test=False):
        """
        入住
        """
        # data = {  # dahuanggg
        #     'room_number':room_id,
        #     'password':password
        # }

        # response = requests.post('http://se.dahuangggg.me:8000/api/conditioners/reception_register_for_customer/',
        #                          data=data
        #                          )
        # if(response.status_code == 200):
        #     return True
        # else:
        #     return False
        print('check_in')
        if test:
            data = {
                'username': '333',
                'password': '333',
                'idCard': idCard,
                'phone': phone,
                'roomType': roomType,
                'days': days,
                'roomNumber': 111
            }
        else:
            data = {
                'username': user_name,
                'password': password,
                'idCard': idCard,
                'phone': phone,
                'roomType': roomType,
                'days': days,
                'roomNumber': roomNumber
            }
        headers = {
            'Authorization': 'Bearer ' + token
        }
        print(f'http://{PATH}/register')
        response = requests.post(f'http://{PATH}/register', json=data, headers=headers)
        if response.status_code == 201:
            print('success')
            return True

    def check_out(self, room_id, token):
        """
        退房
        """
        headers = {
            'Authorization': 'Bearer ' + token
        }
        data = {
            'roomNumber':int(room_id)
        }
        response = requests.post(f'http://{PATH}/check-out',json=data,headers=headers)
        if response.status_code == 201:
            return True,self.check_room_expense(int(room_id),token)
        else:
            return False,None

    def check(self, room_id, start_time='2023-11-21 00:00:00', end_time='2023-11-22 15:45:32'):
        '''
        查看某个房间的详单'api/logs/get_ac_info/'
        '''
        data = {
            'start_time': start_time,
            'end_time': end_time
        }
        response = requests.post('http://10.129.67.27:8000/api/logs/get_ac_info/',
                                 data=data
                                 )
        output = json.loads(response.content)['detail']
        for dict in output:
            if (dict['roomNumber'] == '房间101'):
                detial = dict
        print(detial)

        return True, data

    def check_all_log(self):
        response = requests.get('http://se.dahuangggg.me/api/logs/get_all_logs/')
        data = json.loads(response.content)['log']
        return data

    def check_room_expense(self, room_id, token):
        headers = {
            'Authorization': 'Bearer ' + token
        }
        response = requests.get(f'http://{PATH}/room-details/{int(room_id)}', headers=headers)
        if response.status_code != 200:
            return []
        data = json.loads(response.content)['roomDetails']
        return data

    def getoperate(self):
        """
        查看系统设置
        """
        temp_upper_limit = 10
        temp_lower_limit = 1
        work_modes = ['制冷', '制热', '通风']
        speed_rates = {'low': '0.5', 'medium': '0.75', 'high': '1.0'}
        return temp_upper_limit, temp_lower_limit, work_modes, speed_rates

    def operate_set(self, temp_upper_limit, temp_lower_limit, work_mode, rate_low, rate_medium, rate_high):
        """
        依据传输的内容修改系统设置
        """
        pass
        return True


if __name__ == '__main__':
    acount = log_data(test=True)
    test = hotel_data('test')
    test.check_room_expense(111,acount.token)
    #print(test.room(token=acount.token))
    #test.check_in(token=acount.token, test=True)

