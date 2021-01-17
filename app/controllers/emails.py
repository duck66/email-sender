import http
from app.schemas.emails import EmailsSchema
from marshmallow import ValidationError

from app.models.emails import Emails

def save_emails(data):
    schema = EmailsSchema()
    try:        
        validated_data = schema.load(data)        
    except ValidationError as e:        
        return http.HTTPStatus.BAD_REQUEST, dict(message=str(e))

    email = Emails(**validated_data).save()
    
    return http.HTTPStatus.CREATED, schema.dump(email)