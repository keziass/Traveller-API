from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    dob = fields.Date(required=True)
    address = fields.Str(required=True) 
    status = fields.Str(required=True) 
    created_at = fields.DateTime(required=True)
    last_update = fields.DateTime(required=True) 

class NotificationMessage(Schema):
    code = fields.Int(required=True)
    msg = fields.Str(required=True)

class LoginResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)
    session_id = fields.Str(required=True)
    data = fields.Nested(UserSchema(exclude=('password',)))