from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database_setup import Conditioner, Log, Detail
from extension import db

log = Blueprint('log', __name__)


# 获取特定空调信息
@log.route('/api/logs/get_ac_info/', methods=['GET'])
def get_ac_info():
    try:
        ac_id = request.args.get('ac_id')
        ac = Conditioner.query.get(ac_id)
        if ac:
            return jsonify({
                'temperature_now': ac.temperature_now,
                'temperature_set': ac.temperature_set,
                'mode': ac.mode,
                'status': ac.status,
                'room_number': ac.room_number,
                'update_times': ac.update_times,
                'cost': ac.cost,
                'total_cost': ac.total_cost,
                'queue_status': ac.queue_status,
                'queue_time': ac.queue_time.isoformat()
            }), 200
        else:
            return jsonify({'error': '空调信息不存在'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 获取所有日志信息
@log.route('/api/logs/get_all_logs/', methods=['GET'])
def get_all_logs():
    logs = Log.query.all()
    logs_info = [{
        'id': log.id,
        'type': log.type,
        'time': log.time.isoformat(),
        'operator': log.operator,
        'object_id': log.object_id,
        'remark': log.remark
    } for log in logs]
    return jsonify(logs_info), 200


# 获取房间费用信息
@log.route('/api/logs/get_room_expense/', methods=['GET'])
def get_room_expense():
    room_number = request.args.get('room_number')
    expenses = Detail.query.filter_by(room_number=room_number).all()
    expenses_info = [{
        'cost': expense.cost,
        'total_cost': expense.total_cost,
        'fee': expense.fee
    } for expense in expenses]
    return jsonify(expenses_info), 200


# 获取所有详细信息
@log.route('/api/logs/get_all_details/', methods=['GET'])
def get_all_details():
    details = Detail.query.all()
    details_info = [{
        'room_number': detail.room_number,
        'request_duration': detail.request_duration,
        'start_time': detail.start_time.isoformat(),
        'end_time': detail.end_time.isoformat(),
        'service_duration': detail.service_duration,
        'speed': detail.speed,
        'cost': detail.cost,
        'total_cost': detail.total_cost,
        'fee': detail.fee
    } for detail in details]
    return jsonify(details_info), 200
