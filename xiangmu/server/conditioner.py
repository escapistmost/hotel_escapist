from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database_setup import Conditioner, User
from extension import db

conditioner = Blueprint('conditioner', __name__)


@conditioner.route('/api/conditioners/get_ac_info/', methods=['GET'])
def get_ac_info():
    ac_id = request.args.get('ac_id')
    ac = Conditioner.query.get(ac_id)
    if ac:
        ac_info = {
            'temperature_now': ac.temperature_now,
            'temperature_set': ac.temperature_set,
            'mode': ac.mode,
            'status': ac.status,
            # 其他字段
        }
        return jsonify(ac_info), 200
    else:
        return jsonify({'error': '空调信息不存在'}), 404


@conditioner.route('/api/conditioners/update_ac_info/', methods=['POST'])
def update_ac_info():
    ac_id = request.json.get('ac_id')
    ac = Conditioner.query.get(ac_id)
    if ac:
        ac.temperature_set = request.json.get('temperature_set', ac.temperature_set)
        # 更新其他字段
        db.session.commit()
        return jsonify({'success': '空调信息更新成功'}), 200
    else:
        return jsonify({'error': '空调信息不存在'}), 404


@conditioner.route('/api/conditioners/get_all_ac_info/', methods=['GET'])
def get_all_ac_info():
    all_ac = Conditioner.query.all()
    all_ac_info = [{
        'id': ac.id,
        'temperature_now': ac.temperature_now,
        'temperature_set': ac.temperature_set,
        # 其他字段
    } for ac in all_ac]
    return jsonify(all_ac_info), 200


@conditioner.route('/api/conditioners/admin_update_ac_info/', methods=['POST'])
def admin_update_ac_info():
    ac_id = request.json.get('ac_id')
    ac = Conditioner.query.get(ac_id)
    if ac:
        # 更新字段，例如 ac.mode = request.json.get('mode', ac.mode)
        db.session.commit()
        return jsonify({'success': '管理员更新空调信息成功'}), 200
    else:
        return jsonify({'error': '空调信息不存在'}), 404


@conditioner.route('/api/conditioners/reception_get_room_number/', methods=['GET'])
def reception_get_room_numbers():
    room_numbers = Conditioner.query.with_entities(Conditioner.room_number).distinct()
    return jsonify({'room_numbers': [room.room_number for room in room_numbers]}), 200


@conditioner.route('/api/conditioners/reception_register_for_customer/', methods=['POST'])
def reception_register_for_customer():
    name = request.json.get('name')
    password = request.json.get('password')
    identity = request.json.get('identity')
    new_user = User(name=name, password=password, identity=identity)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'success': '客户注册成功', 'user_id': new_user.id}), 201


@conditioner.route('/api/conditioners/reception_check_out_for_customer/', methods=['POST'])
def reception_check_out_for_customer():
    user_id = request.json.get('user_id')
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'success': '客户退房成功'}), 200
    else:
        return jsonify({'error': '用户不存在'}), 404


@conditioner.route('/api/conditioners/reset/', methods=['POST'])
def reset_all_ac_info():
    conditioners = Conditioner.query.all()
    for ac in conditioners:
        ac.temperature_now = 0
        ac.temperature_set = 0
        # 重置其他字段
    db.session.commit()
    return jsonify({'success': '所有空调信息重置成功'}), 200
