from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("app.config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import emails

from app.blueprints.emails import email_blueprint
app.register_blueprint(email_blueprint)
