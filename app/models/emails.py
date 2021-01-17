import sqlalchemy as sa

from app.models.enums import EmailStatus
from app import db

class BaseModel(db.Model):
    """
    This class is the abstract model that inherited from other model
    """

    __abstract__ = True

    id = sa.Column(sa.Integer(), primary_key=True)
    created_at = sa.Column(
        sa.DateTime(),
        default=sa.func.now(),
        server_default=sa.func.now(),
        nullable=False,
    )
    updated_at = sa.Column(
        sa.DateTime(),
        default=sa.func.now(),
        onupdate=sa.func.now(),
        nullable=False,
        server_default=sa.func.now(),
        server_onupdate=sa.func.now(),
    )
    is_deleted = sa.Column(sa.Boolean(), default=False, server_default="false")
    deleted_at = sa.Column(sa.DateTime(), default=None)

    def save(self) -> "BaseModel":
        try:
            db.session.add(self)
            db.session.commit()
            return self

        except Exception:
            db.session.rollback()
            raise


class Emails(BaseModel):
    __tablename__ = "emails"

    event_id = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(sa.DateTime(), nullable=False)

class EmailRecipients(BaseModel):
    __tablename__ = "email_recipients"

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

class EmailSender(BaseModel):
    __tablename__ = "email_sender"

    email_id = db.Column(db.Integer, sa.ForeignKey("emails.id"), nullable=False)
    recipient_id = db.Column(db.Integer, sa.ForeignKey("email_recipients.id"), nullable=False)
    status = db.Column(
        db.Enum(EmailStatus, name="email_status"),
        nullable=False,
        default=EmailStatus.NEW,
    )
