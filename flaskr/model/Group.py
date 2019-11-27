import enum

from flaskr import db, ma
from .Base import BaseModel

class Group(db.Model, BaseModel):
    """ 组模型
    """
    __tablename__ = "group"

    name = db.Column("name", db.String(32), nullable=False, comment="角色名称")
    leaderId = db.Column("leader_id", db.String, db.ForeignKey('user.id'), nullable=False, comment="队长ID")
    leader = db.relationship("User")
    # menbers = db.relationship('UserGroup')
    # menbers = db.relationship('User', secondary="user_group" )

class GroupSchema(ma.ModelSchema):
    """ 组模式
    """
    class Meta:
        model = Group
