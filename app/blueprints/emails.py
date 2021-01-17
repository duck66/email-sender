from flask import Blueprint
from flask_restful import Api
from app.resources.emails import EmailResource, RecipientResource

email_blueprint = Blueprint("email", __name__, url_prefix="")
email_resource = Api(email_blueprint)

email_resource.add_resource(EmailResource, "/save-emails")
email_resource.add_resource(RecipientResource, "/save-recipients")
