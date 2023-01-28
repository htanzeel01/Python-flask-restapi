from flask import Flask
import os
from flask import render_template # Remove: import Flask
import connexion
from Main.Model.student import db, Student
from Main.Model.classroom import Classroom


application = connexion.App(__name__, specification_dir="./")
application.add_api("swagger.yml")
def create_app(test_config=None):


 app = Flask(__name__,
 instance_relative_config=True)


 if test_config is None:
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DB_URI")
    )
 else:
    app.config.from_mapping(test_config)

 db.app=app
 db.init_app(app)
 return app 