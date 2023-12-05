# 这个文件是用来存储数据库中得到信息的中转用的

class log_data():
    '''
    登录注册部分可能会用到的信息
    '''
    def __init__(self,username,password):
        self.identification='管理员'
        self.verification=True # 是否得到内容
        self.identify=True # 密码是否正确
        self.room_id=101

class hotel_data():
    '''
    酒店管理需要用到的信息
    '''
    def __init__(self,username):
        self.room_id=['101','102','103','104']
        self.nused_id=['101','102']
        self.used_id=['103','104']