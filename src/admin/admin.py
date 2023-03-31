from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from database.database import db
from models.Todo import Todo



def setup_admin(app):
    app.secret_key = "example"
    app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
    admin = Admin(app, name="TODO app", template_mode="bootstrap3")

    admin.add_view(ModelView(Todo, db.session))