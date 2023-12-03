from flask import Flask, render_template, request, redirect, url_for, session, Blueprint

hotel_receptionist = Blueprint('hotel_receptionist', __name__)


@hotel_receptionist.route('/')
def homepage():
    '''
    检查是否是前台，返回前台的首页
    :return: 首页
    '''
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回管理者或者顾客首页
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return url_for('log_and_submit.login')


@hotel_receptionist.route('/query')
def query():
    """
    查询房间状态，返回一个列表
    :return: 列表展示的页面，包括返回的相关内容
    """
    if 'username' in session:
        # 检查是不是前台，是的话返回查询数据库，返回展示页面，不是的话返回管理者或者顾客首页并提示权限不足（？）
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass
    else:
        # 连注册都没注册的话送到登录页面去
        return url_for('log_and_submit.login')


@hotel_receptionist.route('/check_in')
def check_in():
    """
    办理入住，输入相关信息，办理入住，修改状态
    :return: 办理成功或失败的信息
    """
    if 'username' in session:
        # 检查是不是前台，是的话办理入住，返回成功或失败的信息，不是的话返回管理者或者顾客首页并提示权限不足（？）
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass
    else:
        # 连注册都没注册的话送到登录页面去
        return url_for('log_and_submit.login')

@hotel_receptionist.route('/check_out')
def check_out():
    """
    办理退房，将状态修改回最初
    :return: 办理成功或失败的信息
    """
    if 'username' in session:
        # 检查是不是前台，是的话办理退房，返回成功或失败的信息，不是的话返回管理者或者顾客首页并提示权限不足（？）
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass
    else:
        # 连注册都没注册的话送到登录页面去
        return url_for('log_and_submit.login')

@hotel_receptionist.route('/query_all')
def query_all():
    """
    查询全部信息
    :return :信息页面
    """
    if 'username' in session:
        # 检查是不是前台，是的话查询全部信息，返回信息页面，不是的话返回管理者或者顾客首页并提示权限不足（？）
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass
    else:
        # 连注册都没注册的话送到登录页面去
        return url_for('log_and_submit.login')

@hotel_receptionist.route('/print_receipt')
def print_receipt():
    """
    打印收据
    :return :下载excel表格
    """
    if 'username' in session:
        # 检查是不是前台，是的话查询对应房间收据，返回excel表格的下载，不是的话返回管理者或者顾客首页并提示权限不足（？）
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass
    else:
        # 连注册都没注册的话送到登录页面去
        return url_for('log_and_submit.login')

@hotel_receptionist.route('/change')
def change():
    """
    依据方法进入对应房间修改页面或者修改房间内容
    :return :下载excel表格
    """
    if 'username' in session:
        # 检查是不是前台，是的话查询对应房间状态，进入房间修改页面或者修改房间内容，不是的话返回管理者或者顾客首页并提示权限不足（？）
        # if session['username' ]==?:
        #     return render_template('')
        # else:
        #     url_for('customer.homepage')
        pass
    else:
        # 连注册都没注册的话送到登录页面去
        return url_for('log_and_submit.login')