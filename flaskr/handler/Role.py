import json

from flask import abort, Blueprint, flash, g, redirect, render_template, request, url_for, jsonify
from werkzeug.exceptions import abort
from flaskr import db
from flaskr.model.Role import Role, RoleSchema

bp = Blueprint("role", __name__)
schema = RoleSchema()
schemas = RoleSchema(many=True)


@bp.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

@bp.route("/roles", methods=("GET",))
def find_and_count_all():
    """查询多条信息"""
    count = Role.query.count()
    rows = Role.query.all()
    return {
        "count": count,
        "rows": schemas.dump(rows)
    }


@bp.route("/roles/<string:id>", methods=("GET",))
def find_by_pk(id):
    """根据主键查询单条信息"""
    data = Role.query.get(id)
    if data is None:
        abort(404, description="记录不存在")
    return schema.dump(data)


@bp.route("/roles", methods=("POST",))
def single_create():
    """创建单条信息"""
    kwds = request.get_json()
    data = Role(**kwds)
    db.session.add(data)
    db.session.commit()
    return schema.dump(data)
