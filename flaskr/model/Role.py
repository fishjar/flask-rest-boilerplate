import enum

from flaskr import db, ma
from .Base import BaseModel


role_menu = db.Table('role_menu',
                     db.Column('role_id', db.String, db.ForeignKey('role.id')),
                     db.Column('menu_id', db.String, db.ForeignKey('menu.id'))
                     )


class Role(db.Model, BaseModel):
    """ 角色模型
    """
    __tablename__ = "role"

    name = db.Column("name", db.String(32), nullable=False, comment="角色名称")
    menus = db.relationship('Menu', secondary=role_menu, backref="roles")


class RoleSchema(ma.ModelSchema):
    """ 角色模式
    """
    class Meta:
        model = Role
