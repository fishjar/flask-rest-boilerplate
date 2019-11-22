import json

from flask import abort, Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flaskr import db
from flaskr.model.Auth import Auth, AuthSchema
from flaskr.utils.jwt import jwt_decode, jwt_encode

schema = AuthSchema()
schemas = AuthSchema(many=True)


def account():
    """帐号登录"""
    kwds = request.get_json()
    auth_name = kwds.get("userName", None)
    password = kwds.get("password", None)

    if not auth_name or not password:
        abort(401, "缺少参数")

    auth_type = "account"
    auth = Auth.query.filter_by(authType=auth_type, authName=auth_name).first()
    if not auth:
        abort(401, "用户不存在")
    elif not auth.user:
        abort(401, "帐号异常")
    elif not check_password_hash(auth["authCode"], password):
        abort(401, "密码错误")

    token = jwt_encode(auth_id=auth.id, auth_type=auth_type,
                       auth_name=auth.name)
    if not token:
        abort(500, "加密错误")

    return {
        "status": "ok",
        "type": "account",
        "message": "登录成功",
        "authToken": token,
    }
