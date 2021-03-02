from marshmallow import Schema, fields

class LocationImageSchema(Schema):
    id = fields.Int(required=True)
    id_location = fields.Int(required=True)
    image_location = fields.Str(required=True)
    status = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)

class LocationTypesSchema(Schema):
	id = fields.Int(required=True)
	name = fields.Str(required=True)
	status = fields.Str(required=True)
	created_at = fields.Str(required=True)
	updated_at = fields.Str(required=True)

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
	updated_at = fields.Str(required=True)

class CommandResultSchema(Schema):
    status_code = fields.Int(required=True)
    error_msg = fields.Str(required=True)
    data = fields.Dict(required=True)
    
