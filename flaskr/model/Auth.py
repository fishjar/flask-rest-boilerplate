import enum

from flaskr import db, ma
from . import BaseModel
from .User import User

class Auth(db.Model, BaseModel):
    """ 鉴权模型
    """
    __tablename__ = "auth"

    userId = db.Column("user_id", db.String, db.ForeignKey('user.id'), nullable=False, comment="用户ID")
    # user = db.relationship("User", back_populates="auths")
    user = db.relationship("User", backref="auths")
    authType = db.Column("auth_type", db.Enum("account","email","phone","wechat","weibo"), nullable=False, comment="鉴权类型")
    authName = db.Column("auth_name", db.String(128), nullable=False, comment="鉴权名称")
    authCode = db.Column("auth_code", db.String, comment="鉴权识别码")
    verifyTime = db.Column("verify_time", db.DateTime, comment="认证时间")
    expireTime = db.Column("expire_time", db.DateTime, comment="过期时间")
    isEnabled = db.Column("is_enabled", db.Boolean, default=True, comment="是否启用")

class AuthSchema(ma.ModelSchema):
    """ 鉴权模式
    """
    class Meta:
        model = Auth
