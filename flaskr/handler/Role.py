import json

from flask import abort, Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
from werkzeug.exceptions import abort
from flaskr import db
from flaskr.model.Role import Role, RoleSchema

schema = RoleSchema()
schemas = RoleSchema(many=True)


def findAndCountAll():
    """查询多条信息"""
    count = Role.query.count()
    rows = Role.query.all()
    return {
        "count": count,
        "rows": schemas.dump(rows)
    }


def singleCreate():
    """创建单条信息"""
    kwds = request.get_json()
    data = Role(**kwds)
    db.session.add(data)
    db.session.commit()
    return schema.dump(data)


def findByPk(id):
    """根据主键查询单条信息"""
    data = Role.query.get(id)
    if data is None:
        abort(404, description="记录不存在")
    return schema.dump(data)
