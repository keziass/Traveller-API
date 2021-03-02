from nameko.rpc import rpc, RpcProxy
from nameko.web.handlers import http
from werkzeug import Response

import json
import schemas

class GatewayService:
    name = "gateway_service"

    location_rpc = RpcProxy('location_service')
    hotel_rpc = RpcProxy('hotel_service')
    user_rpc = RpcProxy('user_service')
    room_rpc = RpcProxy('room_service')
    travelplan_rpc = RpcProxy('travel_plan_service')

    def __init__(self):
        print("Service Constructor")

    def __del__(self):
        print("Service Destructor")

    @http('GET', '/travelplan')
    def get_all_travelplan(self, request):
        travelplan = self.travelplan_rpc.get_all_travelplan()
        return Response(
            schemas.TravelPlanSchema(many=True).dumps(travelplan),
            mimetype='application/json'
        )
    
    @http('GET', '/travelplan/by_id/<int:id>')
    def get_travelplan_by_id(self, request, id):
        travelplan = self.travelplan_rpc.get_travelplan_by_id(id)
        return Response(
            schemas.TravelPlanSchema().dumps(travelplan),
            mimetype='application/json'
        )
    
    @http('GET', '/travelplan/verify/<int:id>')
    def verify_travelplan(self, request, id):
        travelplan = self.travelplan_rpc.verify_travelplan(id)
        if travelplan:
            return "True"
        else:
            return "False"
    
    @http('GET', '/travelplan/by_userID/<int:id>')
    def get_travelplan_by_userID(self, request, id):
        travelplan = self.travelplan_rpc.get_travelplan_by_userID(id)
        return Response(
            schemas.TravelPlanSchema(many=True).dumps(travelplan),
            mimetype='application/json'
        )
    
    @http('POST', '/travelplan/search')
    def search_travelplan(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        travelplan = self.travelplan_rpc.search_travelplan(datajson)
        return Response(
            schemas.TravelPlanSchema().dumps(travelplan),
            mimetype='application/json'
        )
    
    @http('GET', '/travelplan/last')
    def get_last_travelplan(self, request):
        travelplan = self.travelplan_rpc.get_last_travelplan()
        return Response(
            schemas.TravelPlanSchema().dumps(travelplan),
            mimetype='application/json'
        )

    @http('GET', '/detail_travelplan')
    def get_all_detail_travelplan(self, request):
        travelplan = self.travelplan_rpc.get_all_detail_travelplan()
        return Response(
            schemas.TravelPlanDetailSchema(many=True).dumps(travelplan),
            mimetype='application/json'
        )
    
    @http('GET', '/detail_travelplan/by_id/<int:id>')
    def get_detail_travelplan_by_id(self, request, id):
        travelplan = self.travelplan_rpc.get_detail_travelplan_by_id(id)
        return Response(
            schemas.TravelPlanDetailSchema().dumps(travelplan),
            mimetype='application/json'
        )
    
    @http('GET', '/detail_travelplan/verify/<int:id>')
    def verify_detailtravelplan(self, request, id):
        travelplan = self.travelplan_rpc.verify_detailtravelplan(id)
        if travelplan:
            return "True"
        else:
            return "False"
    
    @http('GET', '/detail_travelplan/by_travelplanID/<int:id>')
    def get_detail_travelplan_by_travelplanID(self, request, id):
        travelplan = self.travelplan_rpc.get_detail_travelplan_by_travelplanID(id)
        return Response(
            schemas.TravelPlanDetailSchema(many=True).dumps(travelplan),
            mimetype='application/json'
        )

    @http('POST', '/detail_travelplan/search')
    def search_detail_travelplan(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        travelplan = self.travelplan_rpc.search_detail_travelplan(datajson)
        return Response(
            schemas.TravelPlanDetailSchema().dumps(travelplan),
            mimetype='application/json'
        )

    @http('POST', '/travelplan')
    def create_travelplan(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        travelplan = self.travelplan_rpc.create_travelplan(datajson['id_user'], datajson['name'], datajson['number_of_people'])
        return Response(
            travelplan
        )

    @http('POST', '/detail_travelplan')
    def create_detailtravelplan(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        travelplan = self.travelplan_rpc.create_detailtravelplan(datajson)
        return Response(
            travelplan
        )

    @http('PUT', '/travelplan/cancel/<int:id>')
    def cancel_travelplan(self, request, id):
        travelplan = self.travelplan_rpc.cancel_travelplan(id)
        return Response(
            travelplan
        )

    @http('PUT', '/travelplan')
    def edit_travelplan(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        travelplan = self.travelplan_rpc.edit_travelplan(datajson['id'], datajson['id_user'], datajson['name'], datajson['number_of_people'])
        return Response(
            travelplan
        )

    @http('PUT', '/detail_travelplan')
    def edit_detailtravelplan(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        travelplan = self.travelplan_rpc.edit_detailtravelplan(datajson)
        return Response(
            travelplan
        )

    @http('POST', '/travelplan/copy')
    def copy_travelplan(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        travelplan = self.travelplan_rpc.copy_travelplan(datajson['id_user'], datajson['id_travel_plan'])
        return Response(
            travelplan
        )


    # ==========================================================
    # -------------------------- HOTEL -------------------------
    # ==========================================================

    @http('GET', '/hotel')
    def get_all_hotels(self, request):
        hotel = self.hotel_rpc.get_all_hotels()
        return Response(
            schemas.HotelSchema(many=True).dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotel/list')
    def list_all_hotels_active_deactive(self, request):
        hotel = self.hotel_rpc.list_all_hotels_active_deactive()
        return Response(
            schemas.HotelSchema(many=True).dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotel/by_id/<int:id>')
    def get_hotel_by_id(self, request, id):
        hotel = self.hotel_rpc.get_hotel_by_id(id)
        return Response(
            schemas.HotelSchema().dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotel/search/<string:name>')
    def search_hotels(self, request, name):
        hotel = self.hotel_rpc.search_hotels(name)
        return Response(
            schemas.HotelSchema(many=True).dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotel/check_active/<int:id_hotel>')
    def check_active_hotel(self, request, id_hotel):
        hotel = self.hotel_rpc.check_active_hotel(id_hotel)
        if hotel:
            return "True"
        else:
            return "False"

    @http('GET', '/hotel/check/<int:id_hotel>')
    def check_hotel(self, request, id_hotel):
        hotel = self.hotel_rpc.check_hotel(id_hotel)
        if hotel:
            return "True"
        else:
            return "False"

    @http('POST', '/hotel')
    def add_hotel(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        hotel = self.hotel_rpc.add_hotel(datajson)
        return Response(
            hotel
        )

    @http('PUT', '/hotel')
    def update_hotel(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        hotel = self.hotel_rpc.update_hotel(datajson['id_hotel'], datajson)
        return Response(
            hotel
        )

    @http('DELETE', '/hotel/<int:id_hotel>')
    def delete_hotel(self, request, id_hotel):
        hotel = self.hotel_rpc.delete_hotel(id_hotel)
        return Response(
            hotel
        )

    @http('GET', '/hotelimage')
    def get_all_images(self, request):
        hotel = self.hotel_rpc.get_all_images()
        return Response(
            schemas.ImageSchema(many=True).dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotelimage/list')
    def get_all_images_active_deactive(self, request):
        hotel = self.hotel_rpc.get_all_images_active_deactive()
        return Response(
            schemas.ImageSchema(many=True).dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotelimage/by_id/<int:id>')
    def get_image_by_hotel_id(self, request, id):
        hotel = self.hotel_rpc.get_image_by_hotel_id(id)
        return Response(
            schemas.ImageSchema().dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotelimage/search/<string:name>')
    def search_hotel_images(self, request, name):
        hotel = self.hotel_rpc.search_hotel_images(name)
        return Response(
            schemas.ImageSchema(many=True).dumps(hotel),
            mimetype='application/json'
        )

    @http('GET', '/hotelimage/check/<int:id_image>')
    def check_hotel_image(self, request, id_image):
        hotel = self.hotel_rpc.check_hotel_image(id_image)
        if hotel:
            return "True"
        else:
            return "False"

    @http('POST', '/hotelimage')
    def add_hotel_image(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        hotel = self.hotel_rpc.add_hotel_image(datajson['id_hotel'], datajson['image_location'])
        return Response(
            hotel
        )

    @http('DELETE', '/hotelimage/<int:id_image>')
    def delete_hotel_image(self, request, id_image):
        hotel = self.hotel_rpc.delete_hotel_image(id_image)
        return Response(
            hotel
        )



    # ==========================================================
    # ------------------------ LOCATION ------------------------
    # ==========================================================

    @http('GET', '/locationimage')
    def get_all_location_image(self, request):
        location = self.location_rpc.get_all_location_image()
        return Response(
            schemas.LocationImageSchema(many=True).dumps(location),
            mimetype='application/json'
        )

    @http('GET', '/locationimage/by_id/<int:id>')
    def get_location_image_by_id(self, request, id):
        location = self.location_rpc.get_location_image_by_id(id)
        return Response(
            schemas.LocationImageSchema().dumps(location),
            mimetype='application/json'
        )

    @http('GET', '/locationimage/by_loc/<int:id>')
    def get_image_by_loc(self, request, id):
        location = self.location_rpc.get_image_by_loc(id)
        return Response(
            schemas.LocationImageSchema(many=True).dumps(location),
            mimetype='application/json'
        )

    @http('DELETE', '/locationimage/<int:id>')
    def delete_location_image(self, request, id):
        location = self.location_rpc.delete_location_image(id)
        return Response(
            location
        )

    @http('POST', '/locationimage')
    def create_location_image(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        location = self.location_rpc.create_location_image(datajson)
        return Response(
            location
        )

    @http('GET', '/locationtype')
    def get_all_location_types(self, request):
        location = self.location_rpc.get_all_location_types()
        return Response(
            schemas.LocationTypesSchema(many=True).dumps(location),
            mimetype='application/json'
        )

    @http('GET', '/locationtype/by_id/<int:id>')
    def get_location_types_by_id(self, request, id):
        location = self.location_rpc.get_location_types_by_id(id)
        return Response(
            schemas.LocationTypesSchema().dumps(location),
            mimetype='application/json'
        )

    @http('POST', '/locationtype')
    def create_location_type(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        location = self.location_rpc.create_location_type(datajson['name'])
        return Response(
            location
        )

    @http('PUT', '/locationtype')
    def edit_location_types(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        location = self.location_rpc.edit_location_types(datajson['name'], datajson['id'])
        return Response(
            location
        )

    @http('DELETE', '/locationtype/<int:id>')
    def delete_location_types(self, request, id):
        location = self.location_rpc.delete_location_types(id)
        return Response(
            location
        )

    @http('GET', '/location')
    def get_all_location(self, request):
        location = self.location_rpc.get_all_location()
        return Response(
            schemas.LocationSchema(many=True).dumps(location),
            mimetype='application/json'
        )

    @http('GET', '/location/by_id/<int:id>')
    def get_location_by_id(self, request, id):
        location = self.location_rpc.get_location_by_id(id)
        return Response(
            schemas.LocationSchema().dumps(location),
            mimetype='application/json'
        )

    @http('POST', '/location/search')
    def search_location(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        location = self.location_rpc.search_location(datajson['idtype'], datajson['name'], datajson['address'], datajson['startjam'], datajson['endjam'], datajson['openjam'], datajson['closejam'], datajson['status'])
        return Response(
            schemas.LocationSchema(many=True).dumps(location),
            mimetype='application/json'
        )

    @http('POST', '/location')
    def create_location(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        location = self.location_rpc.create_location(datajson['idtype'], datajson['name'], datajson['address'], datajson['startjam'], datajson['endjam'], datajson['openjam'], datajson['closejam'], datajson['info'])
        return Response(
            location
        )

    @http('PUT', '/location')
    def edit_location(self, request):
        data = request.get_data(as_text=True)
        datajson = json.loads(data)
        location = self.location_rpc.edit_location(datajson['id'], datajson['idtype'], datajson['name'], datajson['address'], datajson['startjam'], datajson['endjam'], datajson['openjam'], datajson['closejam'], datajson['info'])
        return Response(
            location
        )

    @http('DELETE', '/location/<int:id>')
    def delete_location(self, request, id):
        location = self.location_rpc.delete_location(id)
        return Response(
            location
        )



    # ==========================================================
    # ------------------------ ROOM&FAC ------------------------
    # ==========================================================

    @http('POST', '/room/')
    def create_room(self, request): 
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        room = self.room_rpc.create_room(data['id_hotel'],data['name'],data['capacity'],data['price'],data['number_available'],data['img'],data['status'])
        return Response(
            # schemas.RoomSchema(many=True).dumps(room),
            # mimetype='application/json'
            room
            # "received: {}".format(request.get_data(as_text=True))
            # data['name']        
        )

    @http('PUT', '/room/')
    def edit_room(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        room = self.room_rpc.edit_room(data['id'],data['id_hotel'],data['name'], data['capacity'],data['price'],data['number_available'], data['img'])
        return Response(
            # schemas.RoomSchema(many=True).dumps(room),
            # mimetype='application/json'
            room
        )

    @http('DELETE', '/room/<int:id>')
    def delete_room(self, request, id):
        room = self.room_rpc.delete_room(id)
        return Response(
            # schemas.CommandResultSchema().dumps(room),
            # mimetype='application/json'
            room
        )

    @http('GET', '/room/')
    def get_all_room(self, request):
        room = self.room_rpc.get_all_room()
        return Response(
            schemas.RoomSchema(many=True).dumps(room),
            mimetype='application/json'
        )

    @http('GET', '/room/by_id/<int:id>')
    def get_room_by_id(self, request, id):
        room = self.room_rpc.get_room_by_id(id)
        return Response(
            schemas.RoomSchema().dumps(room),
            mimetype='application/json'
        )

    @http('POST', '/search_room/')
    def search_room(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        room = self.room_rpc.search_room(data['id_hotel'],data['name'],data['capacity'],data['price'],data['number_available'],data['img'],data['status'])
        return Response(
            schemas.LocationSchema(many=True).dumps(room),
            mimetype='application/json'
        )

    @http('POST', '/roomfacility/')
    def create_room_facility(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        room = self.room_rpc.create_room_facility(data['id_room'],data['id_facility'])
        return Response(
            # schemas.CommandResultSchema().dumps(room),
            # mimetype='application/json'
            room
        )

    @http('DELETE', '/roomfacility/<int:id>')
    def delete_room_facility(self, request, id):
        room = self.room_rpc.delete_room_facility(id)
        return Response(
            # schemas.CommandResultSchema().dumps(room),
            # mimetype='application/json'
            room
        )

    @http('GET', '/roomfacility/')
    def get_all_room_facility(self, request):
        room = self.room_rpc.get_all_room_facility()
        return Response(
            # schemas.RoomFacilitySchema(many=True).dumps(room),
            # mimetype='application/json'
            room
        )

    @http('GET', '/roomfacility/by_id/<int:id>')
    def get_room_facility_by_id(self, request, id):
        room = self.room_rpc.get_room_facility_by_id(id)
        return Response(
            # schemas.RoomFacilitySchema().dumps(room),
            # mimetype='application/json'
            room
        )

    @http('POST', '/search_room_facility/')
    def search_room_facility(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        room = self.room_rpc.search_room_facility(data['id_room'],data['id_facility'],data['status'])
        return Response(
            # schemas.LocationSchema(many=True).dumps(room),
            # mimetype='application/json'
            room
        )
        
    @http('POST', '/facility/')
    def create_facility(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        room = self.room_rpc.create_facility(data['name'])
        return Response(
            # schemas.CommandResultSchema().dumps(room),
            # mimetype='application/json'
            room
        )

    @http('DELETE', '/facility/<int:id>')
    def delete_facility(self, request, id):
        room = self.room_rpc.delete_facility(id)
        return Response(
            # schemas.CommandResultSchema().dumps(room),
            # mimetype='application/json'
            room
        )

    @http('POST', '/search_facility/')
    def search_facility(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        room = self.room_rpc.search_facility(data['name'], data['status'])
        return Response(
            # schemas.facilitySchema(many=True).dumps(room),
            # mimetype='application/json'
            room
        )

    @http('GET', '/facility/')
    def get_all_facility(self, request):
        room = self.room_rpc.get_all_facility()
        return Response(
            schemas.facilitySchema(many=True).dumps(room),
            mimetype='application/json'
            # room
        )

    @http('GET', '/facility/by_id/<int:id>')
    def get_facility_by_id(self, request, id):
        room = self.room_rpc.get_facility_by_id(id)
        return Response(
            schemas.LocationSchema().dumps(room),
            mimetype='application/json'
            # room
        )
    

    # ==========================================================
    # -------------------------- USER --------------------------
    # ==========================================================

    @http('GET', '/user/')
    def get_all_user(self, request):
        user = self.user_rpc.get_all_user()
        return Response(
            schemas.UserSchema(many=True).dumps(user),
            mimetype='application/json'
            #user
        )

    @http('GET', '/user/by_id/<int:id>')
    def get_user_by_id(self, request, id):
        user = self.user_rpc.get_user_by_id(id)
        return Response(
            schemas.UserSchema().dumps(user),
            mimetype='application/json'
            #user
        )

    @http('POST', '/user/log_in/')
    def log_in(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        user = self.user_rpc.log_in(data['email'],data['password'])
        return Response(
            schemas.UserSchema().dumps(user),
            mimetype='application/json'
            #user
        )

    @http('POST', '/search_user/')
    def search_user(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        user = self.user_rpc.search_facility(data['name'])
        return Response(
            schemas.UserSchema(many=True).dumps(user),
            mimetype='application/json'
            #user
        )

    @http('POST', '/user/')
    def create_user(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        user = self.user_rpc.create_user(data['email'],data['password'],data['name'],data['gender'],data['dob'],data['address'])
        return Response(
            schemas.CommandResultSchema().dumps(user),
            mimetype='application/json'
            #user
        )

    @http('DELETE', '/user/<int:id>')
    def delete_user(self, request, id):
        user = self.user_rpc.delete_user(id)
        return Response(
            schemas.CommandResultSchema().dumps(user),
            mimetype='application/json'
            #user
        )

    @http('PUT', '/user/')
    def edit_user(self, request):
        data_as_text = request.get_data(as_text=True)
        data = json.loads(data_as_text)
        user = self.user_rpc.edit_user(data['id'],data['email'],data['password'],data['name'],data['gender'],data['dob'],data['address'])
        return Response(
            schemas.CommandResultSchema().dumps(user),
            mimetype='application/json'
            #user
        )

    