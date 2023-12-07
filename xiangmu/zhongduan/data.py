# 这个文件是用来存储数据库中得到信息的中转用的
from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
import requests
import json


class log_data():
    """
    登录注册部分可能会用到的信息
    """

    def __init__(self, username, password):
        self.identification = '管理员'
        self.verification = True  # 是否得到内容
        self.identify = True  # 密码是否正确
        self.room_id = 101


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

    def room(self):
        """
        获取当前房屋的使用信息
        """
        response = requests.get('http://se.dahuangggg.me:8000/api/acounts/get_rooms_name/')
        self.room_id = list(json.loads(response.content).values())[0] # 所有房间号
        response = requests.get('http://se.dahuangggg.me:8000/api/conditioners/reception_get_room_number/')
        self.used_id = list(json.loads(response.content).values())[0] # 没人用的
        self.used_id = [key for key in self.used_id.keys() if self.used_id[key] == False]
        self.nused_id = [item for item in self.room_id if item not in self.used_id]  # 有人在用

    def check_in(self, room_id, password):
        """
        入住
        """
        data = {
            'room_number':room_id,
            'password':password
        }
        
        response = requests.post('http://se.dahuangggg.me:8000/api/conditioners/reception_register_for_customer/',
                                 data=data
                                 )
        if(response.status_code == 200):
            return True
        else:
            return False

    def check_out(self, room_id):
        """
        退房
        """
        data = {
            'room_number':room_id
        }
        response = requests.post('http://se.dahuangggg.me:8000/api/conditioners/reception_check_out_for_customer/',
                                 data=data
                                 )
        data = {'列1': ['值1', '值3'], '列2': ['值2', '值4']}  # 详单信息
        return True, data

    def check(self,room_id,start_time = '2023-11-21 00:00:00',end_time = '2023-11-22 15:45:32'):
        '''
        查看某个房间的详单'api/logs/get_ac_info/'
        '''
        data = {
            'start_time':start_time,
            'end_time':end_time
        }
        response = requests.post('http://10.129.67.27:8000/api/logs/get_ac_info/',
                                 data=data
                                 )
        output = json.loads(response.content)['detail']
        for dict in output:
            if(dict['roomNumber'] == '房间101'):
                detial = dict
        print(detial)

        return True, data


    def check_all_log(self):
        response = requests.get('http://se.dahuangggg.me/api/logs/get_all_logs/')
        data = json.loads(response.content)['log']
        return data
    

    def check_room_expense(self,room_id):
        response = requests.get('http://se.dahuangggg.me/api/logs/get_room_expense/')
        output = json.loads(response.content)['roomExpense']
        for dict_list in output:
            if(dict_list['labels'] == room_id):
                data = dict_list['datasets']
        return True,data
        


    def getoperate(self):
        """
        查看系统设置
        """
        temp_upper_limit=10
        temp_lower_limit=1
        work_modes=['制冷', '制热', '通风']
        speed_rates = {'low': '0.5', 'medium': '0.75', 'high': '1.0'}
        return temp_upper_limit,temp_lower_limit,work_modes,speed_rates

    def operate_set(self,temp_upper_limit, temp_lower_limit, work_mode, rate_low, rate_medium, rate_high):
        """
        依据传输的内容修改系统设置
        """
        pass
        return True
    
    def update_ac(self):
        name = {
            'token':'房间101'
        }
        response = requests.post('http://10.129.67.27:8000/api/conditioners/get_ac_info/',data=name)
        data = json.loads(response.content)
        print(data)
        data['targetTemperature'] = 20
        response = requests.post('http://10.129.67.27:8000/api/conditioners/update_ac_info/',json=data,params={'token':'房间101'})
        print(response.status_code)
        if response.status_code == 200:
            print('更新成功')


if __name__ == '__main__':
    test = hotel_data('test')
    test.update_ac()
