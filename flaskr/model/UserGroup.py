import enum

from flaskr import db, ma
from .Base import BaseModel


class UserGroup(db.Model, BaseModel):
    """ 用户组模型
    """
    __tablename__ = "user_group"

    userId = db.Column("user_id", db.String, db.ForeignKey('user.id'), nullable=False, comment="用户ID")
    # user = db.relationship('User')
    groupId = db.Column("group_id", db.String, db.ForeignKey('group.id'), nullable=False, comment="组ID")
    # group = db.relationship('Group', backref="user_usergroups")
    level = db.Column("level", db.SmallInteger, default=0, comment="级别")
    joinTime = db.Column("join_time", db.DateTime, comment="加入时间")
    

class UserGroupSchema(ma.ModelSchema):
    """ 用户组模式
    """
    class Meta:
        model = UserGroup
