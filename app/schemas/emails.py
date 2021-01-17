from marshmallow import Schema, fields

class EmailsSchema(Schema):
    id = fields.Integer()
    event_id = fields.Integer(required=True, allow_none=False)
    subject = fields.String(required=True, allow_none=False)
    content = fields.String(required=True, allow_none=False)
    timestamp = fields.String(required=True, allow_none=False)

class RecipientsSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, allow_none=False)
    email = fields.String(required=True, allow_none=False)
