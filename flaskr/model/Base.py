import uuid
import datetime
from flaskr import db
from flask import abort


class Column(db.Column):
    """ 字段的基类
    """
    __abstract__ = True

    def __init__(self, *args, **kwargs):
        """接收并挂载验证器"""
        validator = kwargs.pop("validator", None)
        if validator is not None:
            self.validator = validator
        super(Column, self).__init__(*args, **kwargs)


class BaseModel(db.Model):
    """ 模型的基类
    """
    __abstract__ = True

    id = db.Column("id", db.String,  primary_key=True,
                   default=lambda: str(uuid.uuid4()), comment="id")
    createdAt = db.Column("created_at", db.DateTime,
                          default=datetime.datetime.utcnow, comment="创建时间")
    updatedAt = db.Column("update_at", db.DateTime,
                          default=datetime.datetime.utcnow, comment="更新时间")
    deletedAt = db.Column("deleted_at", db.DateTime, comment="删除时间")

    # __mapper_args__ = {
    #     "order_by": createdAt.desc()
    # }

    def __new__(cls, *args, **kwargs):
        """模型验证"""
        errors = []
        for k, v in kwargs.items():
            field = getattr(cls, k, None)
            if field:
                validator = getattr(field, "validator", None)
                if validator:
                    schema, msg = validator
                    try:
                        # 验证格式参考
                        # https://github.com/keleshev/schema
                        schema.validate(v)
                    except Exception as e:
                        errors.append(f'字段[{k}]:{msg or str(e)}')
            else:
                # 模型没有该属性
                # 即使此处不拦截，SQLAlchemy也会抛出异常
                errors.append(f'字段[{k}]:多余的')
                pass
        if errors:
            abort(500, "; ".join(errors))
        return super(BaseModel, cls).__new__(cls)

    def update(self, **kwds):
        """字典更新到模型"""
        # self.__dict__.update(kwds)
        for (k, v) in kwds.items():
            setattr(self, k, v)
