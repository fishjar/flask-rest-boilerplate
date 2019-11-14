import uuid
from flaskr import db


class BaseModel:
    """ 模型的基类
    """
    id = db.Column(db.String,  primary_key=True,
                   default=lambda: str(uuid.uuid4()),)  # ID
