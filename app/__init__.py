from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://emailsender:password@localhost:5438/emailsender'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import emails

from app.blueprints.emails import email_blueprint
app.register_blueprint(email_blueprint)

# from app.routes import routes