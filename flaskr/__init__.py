import os
import click
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Config, DevelopmentConfig

__version__ = (1, 0, 0, "dev")

db = SQLAlchemy()
ma = Marshmallow()


def create_app(config=None):
    """创建APP实例"""
    app = Flask(__name__, instance_relative_config=True)

    # 加载配置信息
    if config is None:
        app.config.from_object(DevelopmentConfig())
    else:
        app.config.update(config)

    # 初始化
    db.init_app(app)
    ma.init_app(app)
    
    # 添加命令
    app.cli.add_command(init_db_command)

    # 加载蓝图
    from flaskr.handler import User
    app.register_blueprint(User.bp)

    return app


def init_db():
    """初始化数据"""
    db.drop_all()
    db.create_all()

    # 插入用户
    from flaskr.model.User import User
    gabe = User(name='gebe')
    db.session.add(gabe)
    db.session.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """执行初始化命令"""
    init_db()
    click.echo("初始化完成!")
