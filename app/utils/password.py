import hashlib


def generate_password(password):
    """
    生成 md5 密码
    :param password:
    :return:
    """
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def verify_password(password, md5_password):
    """
    校验密码是否正确
    :param password:
    :return:
    """
    return password == md5_password
