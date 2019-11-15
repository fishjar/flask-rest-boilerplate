import uuid
import datetime
from flaskr import db


class BaseModel:
    """ 模型的基类
    """
    id = db.Column("id", db.String,  primary_key=True,
                   default=lambda: str(uuid.uuid4()), comment="id")
    createdAt = db.Column("created_at", db.DateTime,
                          default=datetime.datetime.utcnow, comment="创建时间")
    updatedAt = db.Column("update_at", db.DateTime,
                          default=datetime.datetime.utcnow, comment="更新时间")
    deletedAt = db.Column("deleted_at", db.DateTime, comment="删除时间")
