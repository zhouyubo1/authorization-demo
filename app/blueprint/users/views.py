from flask import request

from . import user_bp
from flask import g
from flask_pydantic import validate
from app.checks.users import BaseInfo
from app.utils.password import generate_password, verify_password


@user_bp.route('/register', methods=['POST'])
@validate(body=BaseInfo)
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    # 用户名是否注册
    sql = "select username from user where username = '{}'".format(username)
    cur = g.db
    cur.execute(sql)
    if cur.fetchone():
        return {'message': '用户名已经被注册，请更改用户名', 'status': 40001}
    md5_password = generate_password(password)
    try:
        sql = "insert into user(username, password) values('{}','{}')".format(username, md5_password)
        cur.execute(sql)
        g.con.commit()
        return {'message': 'success', 'status': 200}
    except Exception as e:
        print(e)
        return {'message': '账号注册失败', 'status': 50001}


@user_bp.route('/login', methods=['POST'])
@validate(body=BaseInfo)
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # 查找用户
    sql = "select username, password from user where username = '{}'".format(username)
    cur = g.db
    cur.execute(sql)
    user_info = cur.fetchone()
    if not user_info:
        return {'message': '用户名或密码错误', 'status': 40002}
    md5_password = generate_password(password)
    if not verify_password(user_info[1], md5_password):
        return {'message': '用户名或密码错误', 'status': 40003}

    return {'message': 'success', 'status': 200}