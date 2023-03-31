from flask import Flask
from flask import json, jsonify
from flask import request

from database.database import db
from models.Todo import Todo
from routes.routes import api
from admin.admin import setup_admin

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.create_all()

setup_admin(app)

app.register_blueprint(api, url_prefix = "/api")


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)