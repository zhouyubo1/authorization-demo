from flask import Flask, request
from datetime import datetime

from settings import SECRET_KEY, STATIC_FILE_PATH, PORT
from .db import get_db


def middleware(app):
    @app.before_request
    def inner():
        print(f'{request.url}, 访问时间{datetime.now()}')
        get_db()


def create_app():
    app = Flask(__name__, static_url_path='/static/', static_folder=STATIC_FILE_PATH)
    app.config.SECRET_KEY = SECRET_KEY
    app.config.port = PORT
    # 加载数据库对象，打印路由
    middleware(app)

    # 返回响应后关闭连接
    from .db import close_db
    app.teardown_appcontext(close_db)

    # 注册蓝图
    from app.blueprint.users import user_bp
    app.register_blueprint(user_bp)

    return app