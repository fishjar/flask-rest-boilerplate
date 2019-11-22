import datetime
import jwt
from flask import current_app as app


def jwt_encode(**kwds):
    """jwt加密
    帐号参数：authId, authType, authName
    """
    if not kwds:
        return ""
    secret = app.config.get("JWT_SECRET", "secret")
    try:
        kwds["exp"] = datetime.datetime.utcnow(
        ) + datetime.timedelta(seconds=60*60*24)
        app.logger.info(f'jwt加密：{kwds}')
        s = jwt.encode(kwds, secret, algorithm='HS256')
    except e:
        app.logger.error(f'jwt加密错误：{e}')
        return ""
    return s


def jwt_decode(token):
    """jwt解密"""
    if not token:
        return {}
    secret = app.config.get("JWT_SECRET", "secret")
    try:
        d = jwt.decode(token, secret, algorithm='HS256')
    except jwt.ExpiredSignatureError as e:
        app.logger.error(f'jwt过期：{e}')
        return {}
    return d
