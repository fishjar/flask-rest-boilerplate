import enum
from flaskr import db, ma
from . import BaseModel

class User(db.Model, BaseModel):
    """ 用户模型
    """
    __tablename__ = "user"

    name = db.Column("name", db.String(32), nullable=False, comment="名字")
    nickname = db.Column("nickname", db.String(64), comment="昵称")
    gender = db.Column("gender", db.SmallInteger, comment="性别")


class UserSchema(ma.ModelSchema):
    """ 用户模式
    """
    class Meta:
        model = User
