from flask import g
from settings import MYSQL_SERVER, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
import pymysql
pymysql.install_as_MySQLdb()


conn = pymysql.connect(database=MYSQL_DB, user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_SERVER, port=MYSQL_PORT)


def get_db():
    if 'db' not in g:
        g.db = conn.cursor()
        g.con = conn


def close_db(e=None):
    db = g.pop('db', None)
    con = g.pop('con', None)
    if db is not None:
        db.close()

    if con is not None:
        db.close()

