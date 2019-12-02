import enum

from flaskr import db, ma
from .Base import BaseModel

class Menu(db.Model, BaseModel):
    """ 菜单模型
    """
    __tablename__ = "menu"

    parentId = db.Column("parent_id", db.String, db.ForeignKey('menu.id'), comment="父ID")
    parent = db.relationship("Menu", backref="children", remote_side="Menu.id")
    name = db.Column("name", db.String(32), nullable=False, comment="菜单名称")
    path = db.Column("path", db.String, nullable=False, comment="菜单路径")
    icon = db.Column("icon", db.String, comment="菜单图标")
    sort = db.Column("sort", db.Integer, default=0, comment="排序")


class MenuSchema(ma.ModelSchema):
    """ 菜单模式
    """
    class Meta:
        model = Menu
