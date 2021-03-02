from nameko.rpc import rpc, RpcProxy

import dependencies, schemas

class TravelPlanService:
    # ==========================================================
    # ---------------------- Service Name ----------------------
    # ==========================================================
    
    name = 'travel_plan_service'

    # ==========================================================
    # ----------------------- Dependency -----------------------
    # ==========================================================

    database = dependencies.Database()

    # ==========================================================
    # -------------------------- Proxy -------------------------
    # ==========================================================

    location_rpc = RpcProxy('location_service')
    hotel_rpc = RpcProxy('hotel_service')
    user_rpc = RpcProxy('user_service')

    # ==========================================================
    # ------------------------ Functions -----------------------
    # ==========================================================

    def __init__(self):
        print("Service Constructor")
    
    @rpc
    def get_all_travelplan(self):
        travelplan = self.database.get_all_travelplan()
        self.database.close_connection()
        return schemas.TravelPlanSchema(many=True).dump(travelplan)
    
    @rpc
    def get_travelplan_by_id(self, id):
        travelplan = self.database.get_travelplan_by_id(id)
        self.database.close_connection()
        return schemas.TravelPlanSchema().dump(travelplan)
    
    @rpc
    def verify_travelplan(self, id):
        travelplan = self.database.get_travelplan_by_id(id)
        self.database.close_connection()
        return travelplan['status'] == 'ACTIVE_PUBLIC'
    
    @rpc
    def get_travelplan_by_userID(self, id):
        travelplan = self.database.get_travelplan_by_userID(id)
        self.database.close_connection()
        return schemas.TravelPlanSchema(many=True).dump(travelplan)
    
    @rpc
    def search_travelplan(self, data):
        travelplan = self.database.search_travelplan(data)
        self.database.close_connection()
        return travelplan
    
    @rpc
    def get_last_travelplan(self):
        travelplan = self.database.get_last_travelplan()
        self.database.close_connection()
        return schemas.TravelPlanSchema().dump(travelplan)
    
    @rpc
    def get_all_detail_travelplan(self):
        d_travelplan = self.database.get_all_detail_travelplan()
        self.database.close_connection()
        return schemas.TravelPlanDetailSchema(many=True).dump(d_travelplan)
    
    @rpc
    def get_detail_travelplan_by_id(self, id):
        d_travelplan = self.database.get_detail_travelplan_by_id(id)
        self.database.close_connection()
        return schemas.TravelPlanDetailSchema().dump(d_travelplan)
    
    @rpc
    def verify_detailtravelplan(self, id):
        d_travelplan = self.database.get_detail_travelplan_by_id(id)
        self.database.close_connection()
        return d_travelplan['status'] == 'ACTIVE'
    
    @rpc
    def get_detail_travelplan_by_travelplanID(self, id):
        d_travelplan = self.database.get_detail_travelplan_by_travelplanID(id)
        self.database.close_connection()
        return schemas.TravelPlanDetailSchema(many=True).dump(d_travelplan)

    @rpc
    def search_detail_travelplan(self, data):
        d_travelplan = self.database.search_detail_travelplan(data)
        self.database.close_connection()
        return schemas.TravelPlanDetailSchema().dump(d_travelplan)
    
    @rpc
    def create_travelplan(self, id_user, name, number_of_people):
        result = {
            'err': 0,
            'msg': 'Created!'
        }
        if self.user_rpc.get_user_by_id(id_user):
            self.database.create_travelplan(id_user, name, number_of_people)
            self.database.close_connection()
        else:
               result['err'] = 1
               result['msg'] = 'User ID doesnt exist!'
        return schemas.CommandResultSchema().dumps(result)
    
    @rpc
    def create_detailtravelplan(self, data):
        result = {
            'err': 0,
            'msg': 'Created!'
        }
        if self.database.get_travelplan_by_id(data['id_travel_plan']):
            if self.location_rpc.get_location_by_id(data['id_ref_location']):
                if self.hotel_rpc.get_hotel_by_id(data['id_ref_hotel']):
                    self.database.create_detailtravelplan(data)
                    self.database.close_connection()
                else:
                    result['err'] = 1
                    result['msg'] = 'Hotel ID doesnt exist!'
            else:
                result['err'] = 1
                result['msg'] = 'Location ID doesnt exist!'
        else:
            result['err'] = 1
            result['msg'] = 'Travel Plan ID doesnt exist!'
        return schemas.CommandResultSchema().dumps(result)

    @rpc
    def cancel_travelplan(self, id):
        result = {
            'err': 0,
            'msg': 'Canceled!'
        }
        if self.database.get_travelplan_by_id(id):
            self.database.cancel_travelplan(id)
            d_travelplan = self.database.get_detail_travelplan_by_travelplanID(id)
            for rec in d_travelplan:
                self.database.cancel_detailtravelplan(rec['id'])
            self.database.close_connection()
        else:
            result['err'] = 1
            result['msg'] = 'Travel Plan ID doesnt exist!'
        return schemas.CommandResultSchema().dumps(result)
    
    @rpc
    def edit_travelplan(self, id, id_user, name, number_of_people):
        result = {
            'err': 0,
            'msg': 'Updated!'
        }
        if self.database.get_travelplan_by_id(id):
            if self.user_rpc.get_user_by_id(id_user):
                self.database.edit_travelplan(id, id_user, name, number_of_people)
                self.database.close_connection()
            else:
                result['err'] = 1
                result['msg'] = 'User ID doesnt exist!'
        else:
            result['err'] = 1
            result['msg'] = 'Travel Plan ID doesnt exist!'
        return schemas.CommandResultSchema().dumps(result)
    
    @rpc
    def edit_detailtravelplan(self, data):
        result = {
            'err': 0,
            'msg': 'Updated!'
        }
        if self.database.get_detail_travelplan_by_id(data['id']):
            if self.database.get_travelplan_by_id(data['id_travel_plan']):
                if self.location_rpc.get_location_by_id(data['id_ref_location']):
                    if self.hotel_rpc.get_hotel_by_id(data['id_ref_hotel']):
                        self.database.edit_detailtravelplan(data)
                        self.database.close_connection()
                    else:
                        result['err'] = 1
                        result['msg'] = 'Hotel ID doesnt exist!'
                else:
                    result['err'] = 1
                    result['msg'] = 'Location ID doesnt exist!'
            else:
                result['err'] = 1
                result['msg'] = 'Travel Plan ID doesnt exist!'
        else:
            result['err'] = 1
            result['msg'] = 'Detail Travel Plan ID doesnt exist!'
        return schemas.CommandResultSchema().dumps(result)
    
    @rpc
    def copy_travelplan(self, id_user, id_travel_plan):
        result = {
            'err': 0,
            'msg': 'Copied!'
        }
        if self.user_rpc.get_user_by_id(id_user):
            if self.database.get_travelplan_by_id(id_travel_plan):
                travelplan = self.database.get_travelplan_by_id(id_travel_plan)
                if travelplan['id_user'] != id_user:
                    self.database.create_travelplan(id_user, travelplan['name'], travelplan['number_of_people'])
                    id = self.database.get_last_travelplan()
                    d_travelplan = self.database.get_detail_travelplan_by_travelplanID(id_travel_plan)
                    for rec in d_travelplan:
                        data = {
                            'id_travel_plan': id['id'],
                            'id_ref_location': rec['id_ref_location'],
                            'id_ref_hotel': rec['id_ref_hotel'],
                            'day': rec['day'],
                            'start_hour': rec['start_hour'],
                            'end_hour': rec['end_hour'],
                            'description': rec['description']
                            }
                        self.database.create_detailtravelplan(data)
                    self.database.close_connection()
                else:
                    result['err'] = 1
                    result['msg'] = 'Already exist!'
            else:
                result['err'] = 1
                result['msg'] = 'Travel Plan ID doesnt exist!'
        else:
               result['err'] = 1
               result['msg'] = 'User ID doesnt exist!'
        return schemas.CommandResultSchema().dumps(result)

    def __del__(self):
        print("Service Destructor")