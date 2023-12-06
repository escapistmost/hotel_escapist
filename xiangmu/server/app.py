from flask import Flask
from extension import db
from conditioner import conditioner
from users import users
from log import log
from set_up import set_up
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(conditioner)
    app.register_blueprint(users)
    app.register_blueprint(log)
    app.register_blueprint(set_up)

    return app
