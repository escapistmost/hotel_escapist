# 这个文件是用来存储数据库中得到信息的中转用的

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

    def room(self):
        """
        获取当前房屋的使用信息
        """
        self.room_id = ['101', '102', '103', '104']  # 所有房间号
        self.nused_id = ['101', '102']  # 没人用的
        self.used_id = ['103', '104']  # 有人在用

    def check_in(self, room_id, password):
        """
        入住
        """
        return True

    def check_out(self, room_id):
        """
        退房
        """
        data = {'列1': ['值1', '值3'], '列2': ['值2', '值4']}  # 详单信息
        return True, data

    def check(self,room_id):
        '''
        查看某个房间的详单
        '''
        data = {'列1': ['值1', '值3'], '列2': ['值2', '值4']}  # 详单信息
        return True, data

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