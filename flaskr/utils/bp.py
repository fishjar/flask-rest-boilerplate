def init_app(app):
    """注册蓝图"""
    from flaskr.handler import User, Auth, Role
    # app.register_blueprint(User.bp)
    app.register_blueprint(User.bp)
    app.register_blueprint(Auth.bp)
    app.register_blueprint(Role.bp)
