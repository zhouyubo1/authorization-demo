import os

SECRET_KEY = os.getenv('SECRET_KEY', 'authorization-demo-secret-key')
STATIC_FILE_PATH = os.getenv('STATIC_FILE_PATH', '')

MYSQL_SERVER = os.getenv("MYSQL_SERVER", '127.0.0.1')
MYSQL_PORT= os.getenv("MYSQL_PORT", 3306)
MYSQL_USER = os.getenv("MYSQL_USER", 'sthgadmin')
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", 'Sthg123456')
MYSQL_DB = os.getenv("MYSQL_DB", 'authorization-demo')

SQLALCHEMY_DATABASE_URI = (
    f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}"
)