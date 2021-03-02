from marshmallow import Schema, fields

class RoomSchema(Schema):
    id = fields.Integer(required=True)
    id_hotel = fields.Integer(required=True)
    name = fields.Str(required=True)
    capacity = fields.Float(required=True)
    price = fields.Number(required=True)
    number_available = fields.Int(required=True)
    img = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

class RoomFacilitySchema(Schema):
    id = fields.Integer(required=True)
    id_room = fields.Integer(required=True)
    id_facility = fields.Integer(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

class facilitySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True) 

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)