import http
from app.schemas.emails import EmailsSchema, RecipientsSchema
from marshmallow import ValidationError

from app.models.emails import Emails, EmailRecipients, EmailSender
from app.models.enums import EmailStatus

def save_emails(data):
    schema = EmailsSchema()
    try:        
        validated_data = schema.load(data)        
    except ValidationError as e:
        return http.HTTPStatus.BAD_REQUEST, dict(message=str(e))

    email = Emails(**validated_data).save()

    save_sender(email.id)
    send_email(email.id)
    
    return http.HTTPStatus.CREATED, schema.dump(email)

def save_recipients(data):
    schema = RecipientsSchema()
    try:        
        validated_data = schema.load(data)        
    except ValidationError as e:        
        return http.HTTPStatus.BAD_REQUEST, dict(message=str(e))

    email = EmailRecipients(**validated_data).save()
    
    return http.HTTPStatus.CREATED, schema.dump(email)


def save_sender(email_id : int):
    recipients = EmailRecipients.query.all()
    for data in recipients:
        param = dict(
           email_id=email_id,
           recipient_id=data.id
        )
        EmailSender(**param).save()

def send_email(email_id : int):
    recipients = EmailRecipients.query.all()
    print("Recipient ")
    print(recipients)
    email = Emails.query.filter_by(
        id=email_id
    ).first()
    print("Subject ", email.subject)
    print("Content ", email.content)

    email_sender = EmailSender.query.filter_by(
        email_id=email.id
    ).all()
    for data in email_sender:
        data.status = EmailStatus.SENT.name
        data.save()
