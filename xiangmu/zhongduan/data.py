# 这个文件是用来存储数据库中得到信息的中转用的
from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
import requests
import json

path = '139.59.115.34:5000'


class log_data():
    """
    登录注册部分可能会用到的信息
    """

    def __init__(self, username, password, role):
        self.identification = '管理员'
        self.verification = True  # 是否得到内容
        self.identify = True  # 密码是否正确
        self.room_id = 101
        self.token = self.login(username, password, role)

    def login(self, username, password, role, test=False):
        if test:
            data = {
                'username': '333',
                'password': '333',
                'role': '前台'
            }  # 测试用
        else:
            data = {
                'username': username,
                'password': password,
                'role': role
            }
        response = requests.post(f'http://{path}/login',
                                 json=data
                                 )
        token = json.loads(response.content)['token']
        return token


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
        response = requests.get(f'http://{path}/rooms-available',
                                headers=headers
                                )
        print(response.status_code)
        data = json.loads(response.content)
        self.room_id = [str(dict['number']) for dict in data]
        self.nused_id = [str(dict['number']) for dict in data if dict['occupied'] == False]
        self.used_id = [str(dict['number']) for dict in data if dict['occupied'] == True]
        return self.room_id, self.nused_id, self.used_id

    def check_in(self, room_id, password):
        """
        入住
        """
        data = {
            'room_number': room_id,
            'password': password
        }

        response = requests.post('http://se.dahuangggg.me:8000/api/conditioners/reception_register_for_customer/',
                                 data=data
                                 )
        if (response.status_code == 200):
            return True
        else:
            return False

    def check_out(self, room_id):
        """
        退房
        """

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

    def check_room_expense(self, room_id):
        response = requests.get('http://se.dahuangggg.me/api/logs/get_room_expense/')
        output = json.loads(response.content)['roomExpense']
        for dict_list in output:
            if (dict_list['labels'] == room_id):
                data = dict_list['datasets']
        return True, data

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
    test = hotel_data('test')
    test.login()
    test.room()
    _, data = test.check_out('')
    print(data)
