import enum
from flaskr import db, ma
from . import BaseModel

class Role(db.Model, BaseModel):
    """ 鉴权模型
    """
    __tablename__ = "role"

    name = db.Column("name", db.String(32), nullable=False, comment="角色名称")

class RoleSchema(ma.ModelSchema):
    """ 鉴权模式
    """
    class Meta:
        model = Role
