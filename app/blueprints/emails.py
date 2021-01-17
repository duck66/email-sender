from flask import Blueprint
from flask_restful import Api
from app.resources.emails import EmailResource

email_blueprint = Blueprint("email", __name__, url_prefix="/emails")
email_resource = Api(email_blueprint)

email_resource.add_resource(EmailResource, "")
