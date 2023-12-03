from flask import Flask, render_template, request, redirect, url_for, session, Blueprint


log_and_submit = Blueprint('log_and_submit', __name__)


@log_and_submit.route('/')
def login():
    '''
    进入网页后先登录
    :return: 返回一个本地的网页内容
    '''
    if 'username' in session:
        # return redirect(url_for('')) #导入到对应的首页
        pass
    else:
        return render_template('login.html')


@log_and_submit.route('/submit', methods=['POST'])
def submit():
    '''
    在登陆提交表单后依据表单中的内容确定要转到哪边，并且依据身份建立对应对话session['username']=?，如果是某个房间的使用者session可以加上对应的房间号
    :return:
    '''
    # 这里你可以添加验证逻辑
    username = request.form['username']
    password = request.form['password']
    pass
    # session['username']=? 别忘记建立对话
    # 下面的内容是检查对应账户的信息，没有账户弹出对应的信息，有账户进入对应的页面（房间）
