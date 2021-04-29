from flask import g, current_app
from app.settings import MYSQL_SERVER, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
import pymysql
pymysql.install_as_MySQLdb()


conn = pymysql.connect(database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_SERVER, port=MYSQL_PORT)


def get_db():
    if 'db' not in g:
        g.db = conn.cursor()

    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

