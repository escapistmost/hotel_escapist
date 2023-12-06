from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database_setup import User

hotel_receptionist = Blueprint('users', __name__)
from extension import db

users = Blueprint('users', __name__)


# 用户登录
@users.route('/api/accounts/login/', methods=['POST'])
def login():
    try:
        username = request.json.get('name')
        password = request.json.get('password')
        user = User.query.filter_by(name=username, password=password).first()
        if user:
            return jsonify({'success': '登录成功', 'user_id': user.id}), 200
        else:
            return jsonify({'error': '用户名或密码错误'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 添加用户
@users.route('/api/accounts/add_room/', methods=['POST'])
def add_room():
    try:
        name = request.json.get('name')
        password = request.json.get('password')
        identity = request.json.get('identity')
        new_user = User(name=name, password=password, identity=identity)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': '新用户添加成功', 'user_id': new_user.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 更改密码
@users.route('/api/accounts/change_password/', methods=['POST'])
def change_password():
    try:
        user_id = request.json.get('user_id')
        old_password = request.json.get('old_password')
        new_password = request.json.get('new_password')
        user = User.query.get(user_id)
        if user and user.password == old_password:
            user.password = new_password
            db.session.commit()
            return jsonify({'success': '密码更改成功'}), 200
        else:
            return jsonify({'error': '旧密码错误或用户不存在'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 获取所有用户名称
@users.route('/api/accounts/get_rooms_name/', methods=['GET'])
def get_rooms_name():
    try:
        users = User.query.with_entities(User.id, User.name).all()
        user_names = [{'id': user.id, 'name': user.name} for user in users]
        return jsonify({'users': user_names}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
