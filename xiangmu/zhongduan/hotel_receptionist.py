from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from data import hotel_data

hotel_receptionist = Blueprint('hotel_receptionist', __name__)


# 功能：办理入住，打印某房间详单，退房，查询或修改某房间状态
@hotel_receptionist.route('/')
def homepage():
    '''
    检查是否是前台，返回前台的首页
    :return: 首页
    '''
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回顾客首页
        if session['identification'] == '客户':
            return redirect(url_for('customer.homepage'))
        else:
            return render_template('receptionist_homepage.html', name=session['username'])
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))


@hotel_receptionist.route('/query')
def query():
    """
    查询房间状态，返回一个列表
    :return: 列表展示的页面，包括返回的相关内容
    """
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回顾客首页
        if session['identification'] == '客户':
            return redirect(url_for('customer.homepage'))
        else:
            action = request.args.get('action')
            dic = hotel_data(session['username'])
            if action == 'check_in':
                return render_template('query.html', list1=dic.room_id, list2=dic.nused_id, message='该房间已被使用',
                                       target_url='/receptionist/check_in')
            elif action == 'print_receipt':
                return render_template('query.html', list1=dic.room_id, list2=dic.used_id, message='该房间无人使用',
                                       target_url='/receptionist/print_receipt')
            elif action == 'check_out':
                return render_template('query.html', list1=dic.room_id, list2=dic.used_id, message='该房间无人使用',
                                       target_url='/receptionist/check_out')
            elif action == 'look':
                return render_template('query.html', list1=dic.room_id, list2=dic.room_id, message='啊？',
                                       target_url='/receptionist/look')
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))


@hotel_receptionist.route('/check_in')
def check_in():
    """
    办理入住，输入相关信息，办理入住，修改状态
    :return: 办理成功或失败的信息
    """
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回顾客首页
        if session['identification'] == '客户':
            return redirect(url_for('customer.homepage'))
        else:
            return render_template('receptionist_homepage.html', name=session['username'])
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))


@hotel_receptionist.route('/check_out')
def check_out():
    """
    办理退房，将状态修改回最初
    :return: 办理成功或失败的信息
    """
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回顾客首页
        if session['identification'] == '客户':
            return redirect(url_for('customer.homepage'))
        else:
            dic = hotel_data()
            return render_template('receptionist_homepage.html', name=session['username'])
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))


@hotel_receptionist.route('/query_all')
def query_all():
    """
    查询全部信息
    :return :信息页面
    """
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回顾客首页
        if session['identification'] == '客户':
            return redirect(url_for('customer.homepage'))
        else:
            return render_template('receptionist_homepage.html', name=session['username'])
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))


@hotel_receptionist.route('/print_receipt')
def print_receipt():
    """
    打印收据
    :return :下载excel表格
    """
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回顾客首页
        if session['identification'] == '客户':
            return redirect(url_for('customer.homepage'))
        else:
            return render_template('receptionist_homepage.html', name=session['username'])
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))


@hotel_receptionist.route('/change')
def change():
    """
    依据方法进入对应房间修改页面或者修改房间内容
    :return :下载excel表格
    """
    if 'username' in session:
        # 检查是不是前台，是的话返回前台首页，不是的话返回顾客首页
        if session['identification'] == '客户':
            return redirect(url_for('customer.homepage'))
        else:
            return render_template('receptionist_homepage.html', name=session['username'])
        pass

    else:
        # 连注册都没注册的话送到登录页面去
        return redirect(url_for('log_and_submit.login'))
