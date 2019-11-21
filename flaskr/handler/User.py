import json

from flask import current_app as app
from flask import abort, Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
from werkzeug.exceptions import abort
from flaskr import db
from flaskr.model.User import User, UserSchema
from flaskr.utils.err import InvalidUsage

schema = UserSchema()
schemas = UserSchema(many=True)


# def findAndCountAll():
#     """查询多条信息"""
#     page_num = int(request.args.get('pageNum', '1'))
#     page_size = int(request.args.get('pageSize', '10'))
#     sorter = request.args.getlist('sorter', None)

#     offset = (page_num - 1) * page_size
#     limit = page_size if page_size > 0 else None
#     count = User.query.count()

#     rows = User.query.order_by(User.name, User.nickname).offset(offset).limit(limit).all()
#     # rows = User.query.offset(offset).limit(limit).all()
#     return {
#         "count": count,
#         "rows": schemas.dump(rows)
#     }

def findAndCountAll():
    """查询多条信息"""
    page_num = int(request.args.get('pageNum', '1'))
    page_size = int(request.args.get('pageSize', '10'))
    # sorter = request.args.getlist('sorter', None)
    data = User.query.paginate(
        page=page_num, per_page=page_size, error_out=False)
    return {
        "count": data.total,
        "rows": schemas.dump(data.items),
    }


def singleCreate():
    """创建单条信息"""
    kwds = request.get_json()
    app.logger.info(f'用户提交数据：{kwds}')  # 记录提交的数据
    if kwds.get("name", None) is None:
        # raise InvalidUsage("用户名不能为空", 400)
        abort(400, "用户名不能为空")
    data = User(**kwds)
    db.session.add(data)
    db.session.commit()
    return schema.dump(data)


def findByPk(id):
    """根据主键查询单条信息"""
    # data = User.query.get(id)
    # if data is None:
    #     abort(404, description="记录不存在")
    data = User.query.get_or_404(id)
    return schema.dump(data)


def updateByPk(id):
    """更新单条"""
    data = User.query.get_or_404(id)
    kwds = request.get_json()
    data.update(**kwds)
    db.session.commit()
    return schema.dump(data)


def destroyByPk(id):
    """删除单条"""
    data = User.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return schema.dump(data)
