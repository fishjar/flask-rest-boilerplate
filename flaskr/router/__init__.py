from flask import Blueprint
from flaskr.handler import User, Role, Auth

user = Blueprint("user", "User")
role = Blueprint("role", "Role")
auth = Blueprint("auth", "Auth")

user.add_url_rule("/users", view_func=User.findAndCountAll, methods=("GET",))
user.add_url_rule("/users", view_func=User.singleCreate, methods=("POST",))
user.add_url_rule("/users/<string:id>", view_func=User.findByPk, methods=("GET",))
user.add_url_rule("/users/<string:id>", view_func=User.updateByPk, methods=("PATCH",))
user.add_url_rule("/users/<string:id>", view_func=User.destroyByPk, methods=("DELETE",))

role.add_url_rule("/roles", view_func=Role.findAndCountAll, methods=("GET",))
role.add_url_rule("/roles", view_func=Role.singleCreate, methods=("POST",))
role.add_url_rule("/roles/<string:id>", view_func=Role.findByPk, methods=("GET",))

auth.add_url_rule("/auths", view_func=Auth.findAndCountAll, methods=("GET",))
auth.add_url_rule("/auths", view_func=Auth.singleCreate, methods=("POST",))
auth.add_url_rule("/auths/<string:id>", view_func=Auth.findByPk, methods=("GET",))
