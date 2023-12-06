from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
import requests
import json
customer = Blueprint('customer', __name__)


base_data = {
            'roomNumber': 0,
            'currentTemperature': 0,
            'targetTemperature': 0,
            'acStatus': '',
            'acMode': '',
            'cost': 0,
            'totalCost': 0,
            'queueStatus': '',
        }

@customer.route('/')
def homepage():
    """
    检查是否是房间使用者，返回使用者房间的首页
    :return: 首页
    """
    if 'username' in session:
        if session['identification'] == '客户':
            return 'hello'
        else:
            return render_template('customer_homepage.html')
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return render_template('customer_homepage.html')
        return redirect(url_for('log_and_submit.login'))


@customer.route('/open_condition')
def open_condition():
    """
    依据数据库内容开启或关闭空调（修改对应空调状态）
    :return: 成功开启/关闭空调的信息或者未能成功关闭
    """
    if 'username' in session:
        # 检查是不是房间使用者，是的话依据数据库内容开启或关闭空调（修改对应空调状态），不是的话返回管理者或者前台首页
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))

@customer.route('/air_conditioner/', methods=['POST'])
def update_ac():
    name = {
        'token':'房间101'
    }
    response = requests.post('http://se.dahuangggg.me:8000/api/conditioners/get_ac_info/',data=name)
    data = json.loads(response.content)
    

    for key,value in request.form.to_dict().items():
        print(key,value)
        data[key] = value
    print(type(data))
    #response = requests.post('http://10.129.67.27:8000/api/conditioners/update_ac_info/',data=data,params={'token':'abc'})
    print(response.status_code)
    if(response.status_code == 200):
        print('更新成功')
    return "<h1>{data}<h1>"


@customer.route('/check')
def check():
    """
    检查自身房间的状态
    :return: 房间状态信息页面
    """
    if 'username' in session:
        # 检查是不是房间使用者，是的话查询数据库并返回空调状态页面，不是的话返回管理者或者顾客首页
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))


@customer.route('/change')
def change():
    """
    修改自身房间的状态
    :return: 修改是否成功的信息
    """
    if 'username' in session:
        # 检查是不是房间使用者，是的话依据对应信息进行修改，返回是否成功，不是的话返回管理者或者顾客首页
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))
