from marshmallow import Schema, fields

class HotelSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)
    star = fields.Int(required=True)
    status = fields.Str(required=True)
    created_at = fields.Date(required=True)
    updated_at = fields.Date(required=True)

class ImageSchema(Schema):
    id = fields.Int(required=True)
    id_hotel = fields.Int(required=True)
    image_location = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Date(required=True)
    updated_at = fields.Date(required=True)

class NotificationMessage(Schema):
    code = fields.Int(required=True)
    msg = fields.Str(required=True)