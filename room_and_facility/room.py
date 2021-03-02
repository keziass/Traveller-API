from nameko.rpc import rpc

import dependencies, schemas

class RoomService:

    name = 'room_service'
    database = dependencies.Database()

    def __init__(self):
        print("Service Constructor")

    # ==========================================================
    # --------------------- ROOM FUNCTION ----------------------
    # ------------------- BILLY PANGESTU -----------------------
    # ==========================================================
    @rpc
    def create_room(self, id_hotel, name, capacity, price, number_available, img, status):   
        self.database.create_room(id_hotel, name, capacity, price, number_available, img, status)
        self.database.close_connection()
        result = {
            'msg': 'Berhasil input Database'
        }
        self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)
    @rpc
    def edit_room(self, id, id_hotel, name, capacity, price, number_available, img):
        try:    
            self.database.edit_room(id, id_hotel, name, capacity, price, number_available, img)
            self.database.close_connection()
            result = {
                'msg': 'Berhasil edit Database'
            }
        except:
            result = {
                'msg': 'Gagal edit Database'
            }
        self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def delete_room(self, id):
        self.database.delete_room(id)
        result = {
            'msg': 'Berhasil Delete'
        }
        self.database.close_connection()
        return schemas.CommandResultSchema().dumps(result)
    @rpc
    def get_all_room(self):
        all_room = self.database.get_all_room()
        self.database.close_connection()
        return schemas.RoomSchema(many=True).dump(all_room)

    @rpc
    def get_room_by_id(self, id):
        room = self.database.get_room_by_id(id)
        self.database.close_connection()
        return schemas.RoomSchema().dump(room)

    @rpc
    def search_room(self, id_hotel,name,capacity, price, number_available,img, status):
        search = self.database.search_room(id_hotel,name,capacity, price, number_available,img, status)
        self.database.close_connection()
        return schemas.RoomSchema(many=True).dump(search)

    # ==========================================================
    # ---------------- ROOM FACILITY FUNCTION ------------------
    # ------------------------- SURYA --------------------------
    # ==========================================================
    @rpc
    def create_room_facility(self, id, id_room, id_facility, status):
        room_facility = self.database.create_room_facility(id, id_room, id_facility, status)
        self.database.close_connection()
        return schemas.RoomFacilitySchema().dumps(room_facility)

    @rpc
    def delete_room_facility(self, id):
        room_facility = self.database.delete_room_facility(id)
        self.database.close_connection()
        return schemas.RoomFacilitySchema().dumps(room_facility)

    @rpc
    def get_all_room_facility(self):
        room_facility = self.database.get_all_room_facility()
        self.database.close_connection()
        return schemas.RoomFacilitySchema(many=True).dumps(room_facility)

    @rpc
    def get_room_facility_by_id(self, id):
        room_facility = self.database.get_room_facility_by_id(id)
        self.database.close_connection()
        return schemas.RoomFacilitySchema().dumps(room_facility)

    @rpc
    def get_room_by_id(self, id):
        room_facility = self.database.get_room_by_id(id)
        self.database.close_connection()
        return schemas.RoomFacilitySchema().dumps(room_facility)

    @rpc
    def get_facility_by_id(self, id):
        room_facility = self.database.get_facility_by_id(id)
        self.database.close_connection()
        return schemas.RoomFacilitySchema().dumps(room_facility)

    @rpc
    def update_status(self, id, status):
        self.database.update_status(id, status)

    # ==========================================================
    # ------------------- FACILITY FUNCTION --------------------
    # ---------------------- STEVEN HANS -----------------------
    # ==========================================================
    @rpc
    def create_facility(self, name):
        facility = self.database.create_facility(name)
        self.database.close_connection()
        return schemas.facilitySchema().dumps(facility)
    
    @rpc
    def delete_facility(self, id):
        facility = self.database.delete_facility(id)
        self.database.close_connection()
        return schemas.facilitySchema().dumps(facility)
    
    @rpc
    def search_facility(self, name, status):
        facility = self.database.search_facility(name,status)
        self.database.close_connection()
        return schemas.facilitySchema(many=True).dumps(facility)

    @rpc
    def get_all_facility(self):
        facility = self.database.get_all_facility()
        self.database.close_connection()
        return schemas.facilitySchema(many=True).dump(facility)
    
    @rpc
    def get_facility_by_id(self, id):
        facility = self.database.get_facility_by_id(id)
        self.database.close_connection()
        return schemas.facilitySchema().dump(facility)
    
    @rpc
    def search_facility(self, name):
        facility = self.database.search_facility(name)
        self.database.close_connection()
        return schemas.facilitySchema().dump(facility)

    @rpc
    def verify_facility(self, id):
        facility = self.database.get_facility_by_id(id)
        self.database.close_connection()
        return facility['status'] == 'ACTIVE'

    @rpc
    def update_status(self, id, status):
        self.database.update_status(id, status)

    def __del__(self):
        print("Service Destructor")
