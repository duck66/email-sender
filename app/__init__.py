from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from celery import Celery

app = Flask(__name__)
app.config.from_object("app.config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)

from app.models import emails
from app.blueprints.emails import email_blueprint

app.register_blueprint(email_blueprint)

