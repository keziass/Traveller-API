from nameko.rpc import rpc

import dependencies, schemas

class LocationService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'location_service'

    # ==========================================================
    # ----------------------- Dependency -----------------------
    # ==========================================================

    database = dependencies.Database()

    # ==========================================================
    # ------------------------ Functions -----------------------
    # ==========================================================

    def __init__(self):
        print("Service Constructor")
    
# ========================================================================================
# ----------------------------------- Location Image -------------------------------------
# ========================================================================================

    @rpc
    def get_all_location_image(self):
        location_images = self.database.get_all_location_image()
        self.database.close_connection()
        return schemas.LocationImageSchema(many=True).dump(location_images)
    
    @rpc
    def get_location_image_by_id(self, id):
        location_image = self.database.get_location_image_by_id(id)
        self.database.close_connection()
        return schemas.LocationImageSchema().dump(location_image)
    
    @rpc
    def get_image_by_loc(self, id):
        location_image = self.database.get_image_by_loc(id)
        self.database.close_connection()
        return schemas.LocationImageSchema(many=True).dump(location_image)

    @rpc
    def delete_location_image(self, id):
        result = {
            'status_code': 0,
            'error_msg': 'Image Succesfully Deleted',
            'data': []
        }
        if self.database.get_location_image_by_id(id):
            self.database.delete_location_image(id)
            result['data'].append({'id': id})
        else:
            result['status_code'] = 1
            result['error_msg']= "ID NOT FOUND"
        self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)
    
    @rpc
    def create_location_image(self, data):
        result = {
            'status_code': 0,
            'error_msg': 'Succesfully Created'
        }
        if self.database.create_location_image(data) == 1:
            result['status_code'] = 1
            result['error_msg']= 'Failed to Create Image'
        
        return schemas.CommandResultSchema().dumps(result)

# ========================================================================================
# ----------------------------------- Location Types -------------------------------------
# ========================================================================================

    @rpc
    def get_all_location_types(self):
        loctype = self.database.get_all_location_types()
        self.database.close_connection()
        return schemas.LocationTypesSchema(many=True).dump(loctype)

    @rpc
    def get_location_types_by_id(self, id):
        loctype = self.database.get_location_types_by_id(id,2)
        self.database.close_connection()
        return schemas.LocationTypesSchema().dump(loctype)
    
    @rpc
    def create_location_type(self, name):
        result = {
            'status_code': 0,
            'error_msg': '',
            'data' : []
        }
        print("satu")
        count=self.database.get_location_types_by_name(name, 1)
        print(count)
        if name=='':
            result['status_code'] = 1
            result['error_msg'] = 'Name cannot be NULL'
        elif count['COUNT(*)']>0:
            result['status_code'] = 2
            result['error_msg'] = 'Location Type already exist'
        else:
            self.database.create_location_type(name)
            result['status_code'] = 0
            result['error_msg'] = 'Success'
            id_type = self.database.get_location_types_by_name(name, 2) 
            result['data'].append(id_type)
            print("add6")
        self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)
    
    @rpc
    def edit_location_types(self, name, id):
        result = {
            'status_code': 0,
            'error_msg': '',
            'data' : []
        }
        count=self.database.get_location_types_by_id(id,1)
        count2=self.database.get_location_types_by_name(name, 1)
        print(count['COUNT(*)'])
        if name=='':
            result['status_code'] = 1
            result['error_msg'] = 'Name cannot be NULL'
        elif count['COUNT(*)'] == 0:
            result['status_code'] = 2
            result['error_msg'] = 'Location Type ID not exist'
        elif count2['COUNT(*)']>0:
            result['status_code'] = 3
            result['error_msg'] = 'Location Type name already exist'
        else:
            self.database.edit_location_types(name, id)
            result['status_code'] = 0
            result['error_msg'] = 'Success'
            print("lima")
            id_type = self.database.get_location_types_by_name(name, 2) 
            print("enam")
            result['data'].append(id_type)
            print("tujuh")
        self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)
        
    @rpc
    def delete_location_types(self, id):
        result = {
            'status_code': 0,
            'error_msg': '',
            'data' : []
        }
        count=self.database.get_location_types_by_id(id,1)
        if count['COUNT(*)']==0:
            result['status_code'] = 1
            result['error_msg'] = 'Location Type ID not exist'
        else:
            self.database.delete_location_types(id)
            result['status_code'] = 0
            result['error_msg'] = 'Success'
            print("lima")
            print("enam")
            result['data'].append({'id': id})
            print("tujuh")
        self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)

# ========================================================================================
# -------------------------------------- Location  ---------------------------------------
# ========================================================================================
    @rpc
    def get_all_location(self):
        locs = self.database.get_all_location()
        # self.database.close_connection()
        return schemas.LocationSchema(many=True).dump(locs)

    @rpc
    def get_location_by_id(self, id):
        loc = self.database.get_location_by_id(id)
        #self.database.close_connection()
        return schemas.LocationSchema().dump(loc)

    @rpc
    def search_location(self, idtype, name, address, startjam, endjam, openjam, closejam, status):
        searchloc = self.database.search_location(idtype, name, address, startjam, endjam, openjam, closejam, status)
        #self.database.close_connection()
        return schemas.LocationSchema(many=True).dump(searchloc)

    @rpc
    def create_location(self, idtype, name, address, startjam, endjam, openjam, closejam, info):
        result = {
            'status_code': 0,
            'error_msg': 'Succesfully Created'
        }
        if self.database.create_location(idtype, name, address, startjam, endjam, openjam, closejam, info) == 1:
            result['status_code'] = 1
            result['error_msg']= 'Failed to Create Location'
        #self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)

        #create_loc = self.database.create_location(idtype, name, address, startjam, endjam, openjam, closejam, info)
        #return schemas.LocationSchema().dumps(create_loc)

    @rpc
    def edit_location(self, id, idtype, name, address, startjam, endjam, openjam, closejam, info):
        result = {
            'status_code': 0,
            'error_msg': 'Location Succesfully Updated',
            'data': []
        }
        if self.database.get_location_by_id(id):
            if self.database.edit_location(id, idtype, name, address, startjam, endjam, openjam, closejam, info) == 1:
                result['status_code'] = 1
                result['error_msg']= 'Failed to Update Location'
                result['data'].append({'id': id})
            else :
                result['status_code'] = 0
                result['error_msg']= 'Success to Update Location'
                result['data'].append({'id': id})
        else:
            result['status_code'] = 1
            result['error_msg']= "ID Location Not Found"
            result['data'].append({'id': 'Not Found'})
        #self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)

        #edit_loc = self.database.edit_location(id, idtype, name, address, startjam, endjam, openjam, closejam, info)
        #return schemas.LocationSchema().dumps(edit_loc)
        
    @rpc
    def delete_location(self, id):
        result = {
            'status_code': 0,
            'error_msg': 'Location Succesfully Deleted',
            'data': []
        }
        
        if self.database.get_location_by_id(id):
            self.database.delete_location(id)
            result['data'].append({'id': id})
        else:
            result['status_code'] = 1
            result['error_msg']= "ID Location Not Found"
            result['data'].append({'id': 'Not Found'})
        #self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)

        #delete_loc = self.database.delete_location(id)
        #return schemas.LocationSchema().dumps(delete_loc)


    def __del__(self):
        print("Service Destructor")