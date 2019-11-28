# flask rest bolierplate

## 使用指引

```sh
# 虚拟环境
python3 -m venv venv

# 激活
. venv/bin/activate

# 安装依赖
# pip install Flask
# pip install Flask-SQLAlchemy
# pip install flask-marshmallow
# pip install marshmallow-sqlalchemy
# pip install PyJWT
pip install -r requirements.txt

# 环境变量
export FLASK_APP=flaskr
export FLASK_ENV=development

# 初始化
flask init-db

# 运行
flask run

# 打开一个 Shell
flask shell

# 导出依赖
pip freeze > requirements.txt
```

## 存在问题

- `Relationships` 问题： [参考](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html)
  - 模型相互引用问题，网上很多类似问题：[参考](https://stackoverflow.com/questions/34421205/sqlalchemy-model-circular-import/34503823),[2](https://stackoverflow.com/questions/58095513/flask-sqlalchemy-relationship-error-name-classname-is-not-defined-using-diff)
  - `Menu` 自引用问题，`remote_side=[id]` 的 `id`在`BaseModel`定义，如何引入
  - `User`、`Group`、`UserGroup` 相互引用问题
- 部分错误无法被`_handle_exception`捕获，而是被内置处理器捕获了
- 暂无优雅的数据校验，`sqlalchemy` 推荐的校验方式很繁琐

## 目录结构

```sh
├── flaskr
│   ├── config.py
│   ├── handler
│   │   ├── Auth.py
│   │   ├── Group.py
│   │   ├── __init__.py
│   │   ├── Login.py
│   │   ├── Menu.py
│   │   ├── Role.py
│   │   ├── UserGroup.py
│   │   └── User.py
│   ├── __init__.py
│   ├── model
│   │   ├── Auth.py
│   │   ├── Base.py
│   │   ├── Group.py
│   │   ├── __init__.py
│   │   ├── Menu.py
│   │   ├── Role.py
│   │   ├── UserGroup.py
│   │   └── User.py
│   ├── router
│   │   └── __init__.py
│   └── utils
│       ├── auth.py
│       ├── bp.py
│       ├── cmd.py
│       ├── err.py
│       ├── __init__.py
│       ├── jwt.py
│       └── log.py
├── LICENSE
├── README.md
└── requirements.txt
```