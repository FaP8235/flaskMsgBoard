"""
   初始化实例对象
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
moment = Moment(app)
bootstrap = Bootstrap(app)

from flaskMsgBoard import views, errors, commands
