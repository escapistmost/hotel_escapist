from flask import Flask, request, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from database_setup import Settings
from extension import db

set_up = Blueprint('set_up', __name__)


# 获取和更新设置信息的 API
@set_up.route('/api/setup/settingInfo', methods=['GET', 'POST'])
def setting_info():
    if request.method == 'GET':
        setting = Settings.query.first()  # 获取第一个设置记录
        if setting:
            return jsonify({
                'status': setting.status,
                'mode': setting.mode
                # 包含其他字段
            }), 200
        else:
            return jsonify({'error': '设置信息不存在'}), 404

    elif request.method == 'POST':
        setting_data = request.json
        setting = Settings.query.first()  # 获取第一个设置记录
        if setting:
            setting.status = setting_data.get('status', setting.status)
            setting.mode = setting_data.get('mode', setting.mode)
            # 更新其他字段
            db.session.commit()
            return jsonify({'success': '设置更新成功'}), 200
        else:
            return jsonify({'error': '设置信息不存在'}), 404

    else:
        return jsonify({'error': '不支持的请求方法'}), 405
