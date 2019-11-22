from flask import request


def init_app(app):
    """认证"""
    @app.before_request
    def login_request():
        token = request.headers.get("authorization", "")
        print("-----", token)
