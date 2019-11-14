from flaskr import db, ma
from . import BaseModel


class User(db.Model, BaseModel):
    """ 用户模型
    """
    __tablename__ = "user"

    name = db.Column("name", db.String(20), nullable=True, comment="名字")


class UserSchema(ma.ModelSchema):
    """ 用户模式
    """
    class Meta:
        model = User
