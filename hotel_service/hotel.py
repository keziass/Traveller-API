from nameko.rpc import rpc
import dependencies, schemas


class ImageService:
    name = 'hotel_service'
    database = dependencies.Database()

    def __init__(self):
        print("Service Constructor")

    @rpc
    def get_all_hotels(self):
        hotels = self.database.get_all_active_hotels()
        self.database.close_connection()
        return schemas.HotelSchema(many=True).dump(hotels)

    @rpc
    def list_all_hotels_active_deactive(self):
        hotels = self.database.get_all_hotels()
        self.database.close_connection()
        return schemas.HotelSchema(many=True).dump(hotels)

    @rpc
    def get_hotel_by_id(self, id):
        hotel = self.database.get_hotel_by_id(id)
        self.database.close_connection()
        return schemas.HotelSchema().dump(hotel)

    @rpc
    def search_hotels(self, name):
        hotels = self.database.search_hotels(name)
        self.database.close_connection()
        return schemas.HotelSchema(many=True).dump(hotels)

    @rpc
    def check_active_hotel(self, id_hotel):
        hotel = self.database.get_hotel_by_id(id_hotel)
        self.database.close_connection()
        return hotel['status'] == 'ACTIVE'

    @rpc
    def check_hotel(self, id_hotel):
        hotel = self.database.get_hotel_by_id(id_hotel)
        self.database.close_connection()
        if hotel is None:
            return False
        else:
            return True

    @rpc
    def add_hotel(self, data):
        resultMsg = {
            'code': 200,
            'msg': 'Success to add hotel'
        }
        self.database.add_hotel(data)
        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)

    @rpc
    def update_hotel(self, id_hotel, data):
        resultMsg = {
            'code': 0,
            'msg': ''
        }
        print(self.check_hotel(id_hotel))
        if self.check_hotel(id_hotel):
            resultMsg['code'] = 200
            resultMsg['msg'] = 'Success update data'
            self.database.update_hotel(id_hotel, data)
        else:
            resultMsg['code'] = 404
            resultMsg['msg'] = 'Data hotel not found'

        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)

    @rpc
    def delete_hotel(self, id_hotel):
        resultMsg = {
            'code': 0,
            'msg': ''
        }
        print(self.check_hotel(id_hotel))
        if self.check_hotel(id_hotel):
            resultMsg['code'] = 200
            resultMsg['msg'] = 'Success delete hotel'
            self.database.delete_hotel(id_hotel)
        else:
            resultMsg['code'] = 404
            resultMsg['msg'] = 'Data hotel not found'

        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)

    #-------------------------------------------------------
    #For Image Hotel
    #-------------------------------------------------------

    @rpc
    def get_all_images(self):
        images = self.database.get_all_active_images()
        self.database.close_connection()
        return schemas.ImageSchema(many=True).dump(images)

    @rpc
    def get_all_images_active_deactive(self):
        images = self.database.get_all_images()
        self.database.close_connection()
        return schemas.ImageSchema(many=True).dump(images)

    @rpc
    def get_image_by_hotel_id(self,id):
        image = self.database.get_image_by_hotel_id(id)
        self.database.close_connection()
        return schemas.ImageSchema().dump(image)

    @rpc
    def search_hotel_images(self, name):
        images = self.database.search_hotel_images(name)
        self.database.close_connection()
        return schemas.ImageSchema(many=True).dump(images)

    @rpc
    def check_hotel_image(self, id_image):
        image = self.database.get_image_by_id(id_image)
        self.database.close_connection()
        if image is None:
            return False
        else:
            return True

    @rpc
    def add_hotel_image(self, id_hotel, image_location):
        resultMsg = {
            'code': 0,
            'msg': ''
        }
        print(self.check_active_hotel(id_hotel))
        if self.check_active_hotel(id_hotel):
            resultMsg['code'] = 200
            resultMsg['msg'] = 'Added image hotel'
            self.database.add_hotel_image(id_hotel, image_location)
        else:
            resultMsg['code'] = 404
            resultMsg['msg'] = 'Hotel is not active'

        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)

    @rpc
    def delete_hotel_image(self, id_image):
        resultMsg = {
            'code': 0,
            'msg': ''
        }
        print(self.check_hotel_image(id_image))
        if self.check_hotel_image(id_image):
            resultMsg['code'] = 200
            resultMsg['msg'] = 'Success delete image'
            self.database.delete_hotel_image(id_image)
        else:
            resultMsg['code'] = 404
            resultMsg['msg'] = 'Data image not found'

        self.database.close_connection()
        return schemas.NotificationMessage().dumps(resultMsg)

    def __del__(self):
        print("Service Destructor")