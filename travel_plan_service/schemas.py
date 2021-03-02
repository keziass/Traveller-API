from marshmallow import Schema, fields

class HotelSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)
    star = fields.Float(required=True)
    status = fields.Str(required=True)
    created_at = fields.Date(required=True)
    last_update = fields.Date(required=True)

class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    dob = fields.Date(required=True)
    address = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Date(required=True)
    last_update = fields.Date(required=True)

class LocationSchema(Schema):
    id = fields.Int(required=True)
    id_type = fields.Int(required=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    best_at_start_hour = fields.Date(required=True)
    best_at_end_hour = fields.Date(required=True)
    open_at = fields.Date(required=True)
    close_at = fields.Date(required=True)
    information_url = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Date(required=True)
    last_update = fields.Date(required=True)

class TravelPlanSchema(Schema):
    id = fields.Int(required=True)
    id_user = fields.Int(required=True)
    name = fields.Str(required=True)
    number_of_people = fields.Int(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    last_update = fields.Str(required=True)

class TravelPlanDetailSchema(Schema):
    id = fields.Int(required=True)
    id_travel_plan = fields.Int(required=True)
    id_ref_location = fields.Int(required=True)
    id_ref_hotel = fields.Int(required=True)
    day = fields.Int(required=True)
    start_hour = fields.Str(required=True)
    end_hour = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    last_update = fields.Str(required=True)

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)