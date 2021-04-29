from flask import Flask, request
from datetime import datetime

from app.settings import SECRET_KEY, STATIC_FILE_PATH, PORT


def show_request_info(app):
    @app.before_request
    def inner():
        print(f'{request.url}, 访问时间{datetime.now()}')


def create_app():
    app = Flask(__name__, static_url_path='/api', static_folder=STATIC_FILE_PATH)
    app.config.SECRET_KEY = SECRET_KEY
    app.config.port = PORT
    show_request_info(app)

    # 返回响应后关闭连接
    from .db import close_db
    app.teardown_appcontext(close_db)

    # 注册蓝图
    from app.bp_models.users import user_bp
    app.register_blueprint(user_bp)

    return app