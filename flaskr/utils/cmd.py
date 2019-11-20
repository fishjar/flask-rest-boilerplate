import click
from flask.cli import with_appcontext


def init_app(app):
    """初始化"""
    app.cli.add_command(init_db_command)


@click.command("init-db")
@with_appcontext
def init_db_command():
    """数据初始化"""
    init_db()
    click.echo("初始化完成!")


def init_db():
    """插入初始数据"""
    from flaskr import db

    db.drop_all()
    db.create_all()

    # 插入用户
    from flaskr.model.User import User
    gabe = User(name='gabe')
    jack = User(name='jack')
    rose = User(name='rose')
    # db.session.add(gabe)
    # db.session.add(jack)
    # db.session.add(rose)
    db.session.add_all([gabe, jack, rose])
    db.session.commit()

    # 插入角色
    from flaskr.model.Role import Role
    adminRole = Role(name='admin')
    userRole = Role(name='user')
    guestRole = Role(name='guest')
    db.session.add_all([adminRole, userRole, guestRole])
    db.session.commit()

    # 关联角色
    gabe.roles = [adminRole, userRole, guestRole]
    jack.roles = [userRole, guestRole]
    rose.roles = [guestRole]
    db.session.commit()

    # 插入帐号
    from flaskr.model.Auth import Auth
    auth = Auth(userId=gabe.id, authType="account", authName=gabe.name,)
    db.session.add(auth)
    db.session.commit()
