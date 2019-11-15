import json

from flask import abort, Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
from werkzeug.exceptions import abort
from flaskr import db
from flaskr.model.User import User, UserSchema

bp = Blueprint("user", __name__)
schema = UserSchema()
schemas = UserSchema(many=True)


@bp.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@bp.route("/users", methods=("GET",))
def find_and_count_all():
    """查询多条信息"""
    count = User.query.count()
    rows = User.query.all()
    return {
        "count": count,
        "rows": schemas.dump(rows)
    }


@bp.route("/users/<string:id>", methods=("GET",))
def find_by_pk(id):
    """根据主键查询单条信息"""
    data = User.query.get(id)
    if data is None:
        abort(404, description="记录不存在")
    return schema.dump(data)


@bp.route("/users", methods=("POST",))
def single_create():
    """创建单条信息"""
    kwds = request.get_json()
    data = User(**kwds)
    db.session.add(data)
    db.session.commit()
    return schema.dump(data)
