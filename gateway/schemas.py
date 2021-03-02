from marshmallow import Schema, fields

class HotelSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    address = fields.Str(required=True)
    star = fields.Float(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    last_update = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    gender = fields.Str(required=True)
    dob = fields.Str(required=True)
    address = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    last_update = fields.Str(required=True)

class LocationSchema(Schema):
    id = fields.Int(required=True)
    id_type = fields.Int(required=True)
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    best_at_start_hour = fields.Str(required=True)
    best_at_end_hour = fields.Str(required=True)
    open_at = fields.Str(required=True)
    close_at = fields.Str(required=True)
    information_url = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    last_update = fields.Str(required=True)

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

class ImageSchema(Schema):
    id = fields.Int(required=True)
    id_hotel = fields.Int(required=True)
    image_location = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)

class LocationImageSchema(Schema):
    id = fields.Int(required=True)
    id_location = fields.Int(required=True)
    image_location = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)

class LocationTypesSchema(Schema):
	id = fields.Int(required=True)
	name = fields.Str(required=True)
	status = fields.Str(required=True)
	created_at = fields.Str(required=True)
	updated_at = fields.Str(required=True)

class RoomSchema(Schema):
    id = fields.Integer(required=True)
    id_hotel = fields.Integer(required=True)
    name = fields.Str(required=True)
    capacity = fields.Float(required=True)
    price = fields.Number(required=True)
    number_available = fields.Int(required=True)
    img = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)

class RoomFacilitySchema(Schema):
    id = fields.Integer(required=True)
    id_room = fields.Integer(required=True)
    id_facility = fields.Integer(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)

class facilitySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True) 

class CommandResultSchema(Schema):
    err = fields.Int(required=True)
    msg = fields.Str(required=True)