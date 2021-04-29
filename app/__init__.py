from flask import Flask, request
from datetime import datetime

from app.settings import SECRET_KEY, STATIC_FILE_PATH, SQLALCHEMY_DATABASE_URI


def show_request_info(app):
    @app.before_request
    def inner():
        print(f'{request.url}, 访问时间{datetime.now()}')


def create_app():
    app = Flask(__name__, static_url_path='/api', static_folder=STATIC_FILE_PATH)
    app.config.SECRET_KEY = SECRET_KEY
    app.config.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

    show_request_info(app)

    # 注册蓝图
    from app.bp_models.users import user_bp
    app.register_blueprint(user_bp)

    return app