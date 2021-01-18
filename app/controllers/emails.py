import http
from app.schemas.emails import EmailsSchema, RecipientsSchema
from marshmallow import ValidationError

from datetime import timedelta, datetime
from app.models.emails import Emails, EmailRecipients, EmailSender
from app.models.enums import EmailStatus
from app import celery

def save_emails(data):
    schema = EmailsSchema()
    try:
        validated_data = schema.load(data)        
    except ValidationError as e:
        return http.HTTPStatus.BAD_REQUEST, dict(message=str(e))

    email = Emails(**validated_data).save()
    # eta = datetime.utcnow() + timedelta(seconds=5)

    save_sender(email.id)
    send_email.apply_async((email.id,), eta=email.timestamp - timedelta(hours=7))

    # WORK
    # send_email.apply_async((email.id,),countdown=10)
    # WORK
    
    # send_email.delay(email.id)

    return http.HTTPStatus.CREATED, schema.dump(email)

def save_recipients(data):
    schema = RecipientsSchema()
    try:        
        validated_data = schema.load(data)        
    except ValidationError as e:
        return http.HTTPStatus.BAD_REQUEST, dict(message=str(e))

    email = EmailRecipients(**validated_data).save()

    return http.HTTPStatus.CREATED, schema.dump(email)

# Deprecated
# @celery.task
def save_sender(email_id : int):
    recipients = EmailRecipients.query.all()
    for data in recipients:
        param = dict(
           email_id=email_id,
           recipient_id=data.id
        )
        EmailSender(**param).save()

@celery.task
def send_email(email_id : int):
    recipients = EmailRecipients.query.all()
    print("Recipient ")
    print(recipients)
    email = Emails.query.filter_by(
        id=email_id
    ).first()
    print("Subject ", email.subject)
    print("Content ", email.content)
    print("Datetime ", datetime.now())

    # Deprecated
    email_sender = EmailSender.query.filter_by(
        email_id=email.id
    ).all()
    for data in email_sender:
        data.status = EmailStatus.SENT.name
        data.save()
