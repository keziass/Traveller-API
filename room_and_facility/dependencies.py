from nameko.extensions import DependencyProvider

import pymysqlpool
import pymysql

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection

    # ==========================================================
    # --------------------- ROOM FUNCTION ----------------------
    # ------------------- BILLY PANGESTU -----------------------
    # ==========================================================
    def create_room(self, id_hotel, name, capacity, price, number_available, img, status):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO rooms VALUES(default, '{}', '{}', '{}', '{}', '{}', '{}','{}', default, default)".format(id_hotel, name, capacity, price, number_available, img, status)
        cursor.execute( sql)
        self.connection.commit()

    def edit_room(self, id, id_hotel, name, capacity, price, number_available, img):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = """UPDATE rooms SET
        id_hotel = '{}', 
        name = '{}',
        capacity = '{}',
        price = '{}',
        number_available = '{}',
        img = '{}' 
        WHERE id = '{}'""".format(id_hotel, name, capacity, price, number_available, img, id)
        cursor.execute( sql)
        self.connection.commit()

    def delete_room(self,id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM rooms WHERE id = %s"
        cursor.execute(sql, id)
        self.connection.commit()

    def get_all_room(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM rooms"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_hotel': row['id_hotel'],
                'name': row['name'],
                'capacity': row['capacity'],
                'price': row['price'],
                'number_available': row['number_available'],
                'img': row['img'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def get_room_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM rooms WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def search_room(self, id_hotel,name,capacity, price, number_available,img, status):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = """SELECT * FROM rooms 
        WHERE 
        id_hotel LIKE '%{}%'
        OR name LIKE '%{}%'
        OR capacity LIKE '%{}%' 
        OR price Like '%{}%' 
        OR number_available LIKE '%{}%'
        OR img like '%{}%'
        OR status like '%{}%'""".format(id_hotel,name,capacity,price,number_available,img,status)
        cursor.execute(sql)
        result = []
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_hotel': row['id_hotel'],
                'name': row['name'],
                'capacity': row['capacity'],
                'price': row['price'],
                'number_available': row['number_available'],
                'img': row['img'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    # ==========================================================
    # ---------------- ROOM FACILITY FUNCTION ------------------
    # ------------------------- SURYA --------------------------
    # ==========================================================
    def get_all_room_facility(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM room_facilities"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_room': row['id_room'],
                'id_facility': row['id_facility'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def get_room_facility_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM room_facilities WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    #def get_room_facility_by_status(self, status)

    def get_room_by_id(self, id_room):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM rooms WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_facility_by_id(self, id_facility):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM facilities WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def create_room_facility(self, id, id_room, id_facility, status):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO room_facilities VALUES(default, '{}', '{}', 'Active')"
        cursor.execute(sql)
        self.connection.commit()

    def delete_room_facility(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM room_facilities WHERE id = {}".format(id)
        cursor.execute(sql)
        self.connection.commit()

    # ==========================================================
    # ------------------- FACILITY FUNCTION --------------------
    # ---------------------- STEVEN HANS -----------------------
    # ==========================================================
    def create_facility(self, name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO facilities (id,name) VALUES(null, '{}');". format(name)
        cursor.execute(sql)
        self.connection.commit()
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def delete_facility(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "DELETE FROM facilities where id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def search_facility(self, name, status):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor) 
        sql = "SELECT * FROM facilities WHERE name LIKE '%{}%' OR status LIKE '%{}%'".format(name, status)
        cursor.execute(sql)
        result=[]
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def get_all_facility(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM facilities"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'name': row['name'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_facility_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM facilities WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result
    
    # def search_facility_(self, name):
    #     cursor = self.connection.cursor(pymysql.cursors.DictCursor)
    #     sql = "SELECT * FROM facilities WHERE name = {}".format(name)
    #     cursor.execute(sql)
    #     result = cursor.fetchone()
    #     cursor.close()
    #     return result
        
    def close_connection(self):
        self.connection.close()
        

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        config={'host':'localhost', 'user':'root', 'password':'', 'database':'traveller', 'autocommit':True}
        self.connection_pool = pymysqlpool.ConnectionPool(size=2, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")

         
