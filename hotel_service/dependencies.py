from nameko.extensions import DependencyProvider

import pymysqlpool
import pymysql

#Database Wrapper
class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Construction")
        self.connection = connection

    def get_all_active_hotels(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        results = []
        querysql = "SELECT * FROM hotels WHERE status = 'ACTIVE'"
        cursor.execute(querysql)
        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'name': row['name'],
                'email': row['email'],
                'address': row['address'],
                'star': row['star'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return results

    def get_all_hotels(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        results = []
        querysql = "SELECT * FROM hotels"
        cursor.execute(querysql)
        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'name': row['name'],
                'email': row['email'],
                'address': row['address'],
                'star': row['star'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return results

    def get_hotel_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "SELECT * FROM hotels WHERE id = {}".format(id)
        cursor.execute(querySql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def search_hotels(self, name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "SELECT * FROM hotels WHERE name LIKE '%{}%' AND status = 'ACTIVE'".format(name)
        cursor.execute(querySql)
        results = []

        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'name': row['name'],
                'email': row['email'],
                'address': row['address'],
                'star': row['star'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return results

    def add_hotel(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "INSERT INTO hotels (id, name, email, address, star, status) " \
                   "VALUES(default, %s, %s, %s, %s, 'ACTIVE')"
        cursor.execute(querySql, (
            data['name'],
            data['email'],
            data['address'],
            data['star'],
        ))
        self.connection.commit()

    def update_hotel(self, id_hotel, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "UPDATE hotels SET name = %s, email = %s, address = %s, star = %s, updated_at=default WHERE id = %s "
        cursor.execute(querySql, (
            data['name'],
            data['email'],
            data['address'],
            data['star'],
            id_hotel
        ))
        cursor.close()
        self.connection.commit()

    def delete_hotel(self, id_hotel):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "UPDATE hotels SET status = 'DELETED', updated_at=default WHERE id = %s "
        cursor.execute(querySql, (id_hotel))
        cursor.close()
        self.connection.commit()

    # --------------------------------------------------------------------------
    # For Image Hotel
    # --------------------------------------------------------------------------

    def get_all_active_images(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        results = []
        sql = "SELECT * FROM hotel_images WHERE status = 'ACTIVE'"
        cursor.execute(sql)
        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'id_hotel': row['id_hotel'],
                'image_location': row['image_location'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return results

    def get_all_images(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        results = []
        sql = "SELECT * FROM hotel_images"
        cursor.execute(sql)
        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'id_hotel': row['id_hotel'],
                'image_location': row['image_location'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return results

    def get_image_by_id(self, id_image):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "SELECT * FROM hotel_images WHERE id = {}".format(id_image)
        cursor.execute(querySql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_image_by_hotel_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "SELECT * FROM hotel_images WHERE id_hotel = {}".format(id)
        cursor.execute(querySql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def search_hotel_images(self, name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        results = []
        sql = "SELECT * FROM hotel_images JOIN hotels ON hotel_images.id_hotel = hotels.id " \
              "WHERE hotels.name LIKE '%{}%' AND hotels.status = 'ACTIVE' AND hotel_images.status = 'ACTIVE'".format(name)
        cursor.execute(sql)
        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'id_hotel': row['id_hotel'],
                'image_location': row['image_location'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return results

    def add_hotel_image(self, id_hotel, image_location):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "INSERT INTO hotel_images (id, id_hotel,image_location, status) " \
              "VALUES (default, %s, %s,'ACTIVE')"
        cursor.execute(sql, (id_hotel, image_location))
        self.connection.commit()

    def delete_hotel_image(self, id_image):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "UPDATE hotel_images SET status = 'DELETED', updated_at=default WHERE id = %s "
        cursor.execute(querySql, (id_image))
        cursor.close()
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

#Dependency Provider
class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        config={
            'host':'127.0.0.1',
            'user':'root', 'password':'',
            'database':'traveller',
            'autocommit':True
        }
        self.connection_pool = pymysqlpool.ConnectionPool(size=5, name='DB Pool', **config)

    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())

    def __del__(self):
        print("DB Dependency Destructor")