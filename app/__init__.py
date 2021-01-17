from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://emailsender:password@localhost:5438/emailsender'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import emails
from app.routes import routes