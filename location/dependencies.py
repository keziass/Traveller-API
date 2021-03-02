from nameko.extensions import DependencyProvider

import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
import datetime

# ========================================================================================
# ----------------------------------- Database Wrapper -----------------------------------
# ========================================================================================

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection
    
# ========================================================================================
# ----------------------------------- Location Image -------------------------------------
# ========================================================================================

    def get_all_location_image(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM location_images WHERE status = 'ACTIVE'"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_location': row['id_location'],
                'image_location': row['image_location'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_location_image_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM location_images WHERE status = 'ACTIVE' AND id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_image_by_loc(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM location_images WHERE status = 'ACTIVE' AND id_location = {}".format(id)
        print(sql)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_location': row['id_location'],
                'image_location': row['image_location'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def delete_location_image(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE location_images SET status = 'DELETED', updated_at = %s WHERE id = %s"
        dt = datetime.datetime.now()
        dt_string = dt.strftime("%Y/%m/%d %H:%M:%S")
        print("DATE", dt_string)
        cursor.execute(sql, (dt_string, id))
        cursor.close()
        self.connection.commit()

    def create_location_image(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO location_images VALUES(default, %s, %s, 'ACTIVE', %s, %s)"
        dt = datetime.datetime.now()
        dt_string = dt.strftime("%Y/%m/%d %H:%M:%S")
        try:
            cursor.execute( sql, 
                            (
                                data['id_location'], 
                                data['image_location'], 
                                dt_string, dt_string
                            )
                        )
            return 0
        except:
            return 1
        
        self.connection.commit()

# ========================================================================================
# ----------------------------------- Location Types -------------------------------------
# ========================================================================================

    def get_all_location_types(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM location_types WHERE status='ACTIVE'"
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

    def get_location_types_by_id(self, id,type):
        if type == 1:
            cursor = self.connection.cursor(dictionary=True)
            print("tiga")
            sql = "SELECT COUNT(*) FROM location_types WHERE id = {}".format((id))
            print("empat")
            cursor.execute(sql)
            print("lima")
            result = cursor.fetchone()
            print("enam")
            cursor.close()
            print("tujuh")
        else:
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT * FROM location_types WHERE id = {}".format((id))
            cursor.execute(sql)
            result = cursor.fetchone()
            cursor.close()
        return result
    
    def get_location_types_by_name(self, name, type):
        print("dua")
        if type == 1:
            cursor = self.connection.cursor(dictionary=True)
            print("tiga")
            sql = "SELECT COUNT(*) FROM location_types WHERE name like '{}'".format((name))
            print("empat")
            # print(cursor.execute(sql))
            cursor.execute(sql)
            print("lima")
            result = cursor.fetchone()
            print("enam")
            cursor.close()
            print("tujuh")
        else:
            print("eadd1")
            cursor = self.connection.cursor(dictionary=True)
            sql = "SELECT id FROM location_types WHERE name like '{}'".format((name))
            print("eadd2")
            cursor.execute(sql) 
            print("eadd3")
            result = cursor.fetchone()
            print("eadd4")
            cursor.close()
            print("eadd5")
        return result
        

    def create_location_type(self, name):
        cursor = self.connection.cursor(dictionary=True)
        print("satu")
        status='ACTIVE'
        sql = "INSERT INTO location_types VALUES(default, %s, %s, %s, %s)"
        print("dua")
        cursor.execute( sql, 
                        (
                            name, 
                            status, 
                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        )
                    )
        print("tiga")
        self.connection.commit()
        print("empat")
    
    def edit_location_types(self, name, id):
        cursor = self.connection.cursor(dictionary=True)
        print("satu")
        sql = "UPDATE location_types SET name = %s, updated_at = %s  WHERE id = %s"
        print("dua")
        cursor.execute(sql, 
                        (
                            name, 
                            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            id
                        )
                    )
        print("tiga")
        self.connection.commit()
        print("empat")

    def delete_location_types(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE location_types SET status = %s, updated_at = %s  WHERE id = %s"
        cursor.execute(sql, ('DELETED', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id))
        cursor.close()
        self.connection.commit()
    
    def close_connection(self):
        self.connection.close()

# ========================================================================================
# -------------------------------------- Location  ---------------------------------------
# ========================================================================================

    def get_all_location(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM locations WHERE status='ACTIVE'"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_type': row['id_type'],
                'name': row['name'],
                'address': row['address'],
                'best_at_start_hour': row['best_at_start_hour'],
                'best_at_end_hour': row['best_at_end_hour'],
                'open_at': row['open_at'],
                'close_at': row['close_at'],
                'information_url': row['information_url'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def search_location(self, idtype, name, address, startjam, endjam, openjam, closejam, status):
        # Startnya = datetime.time(startjam).strftime("%I:00:00")
        # Endnya = datetime.time(endjam).strftime("%I:00:00")
        # Opennya = datetime.time(openjam).strftime("%I:00:00")
        # Closenya = datetime.time(closejam).strftime("%I:00:00")
        # print("Start : " + Startnya)
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM locations WHERE id_type=%s OR name LIKE %s OR address LIKE %s OR best_at_start_hour LIKE %s OR best_at_end_hour LIKE %s OR open_at LIKE %s OR close_at LIKE %s OR status LIKE %s"
        cursor.execute(sql, (idtype,name,address,startjam, endjam, openjam, closejam, status))
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_type': row['id_type'],
                'name': row['name'],
                'address': row['address'],
                'best_at_start_hour': row['best_at_start_hour'],
                'best_at_end_hour': row['best_at_end_hour'],
                'open_at': row['open_at'],
                'close_at': row['close_at'],
                'information_url': row['information_url'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def get_location_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM locations WHERE id = {}".format((id))
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def create_location(self, idtype, name, address, startjam, endjam, openjam, closejam, info):
        print("ID Type : " , int(idtype))
        print("Name : " + name)
        print("Address : " + address)
        print("Start Jam : " , int(startjam))
        print("End Jam : " , int(endjam))
        print("Open Jam : " , int(openjam))
        print("Close Jam : " , int(closejam))
        print("Info URL : " + info)
        
        cursor = self.connection.cursor(dictionary=True)
        status='ACTIVE'
        sql = "INSERT INTO locations VALUES(default, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try :
            cursor.execute( sql, 
                            (
                                idtype,
                                name,
                                address,
                                datetime.time(startjam).strftime("%I:00:00"),
                                datetime.time(endjam).strftime("%I:00:00"),
                                datetime.time(openjam).strftime("%I:00:00"),
                                datetime.time(closejam).strftime("%I:00:00"),
                                info, 
                                status, 
                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            )
                        )
            print("Berhasil Masuk Database")
            self.connection.commit()
            return 0
        except :
            print("Tidak Berhasil Masuk Database")
            return 1
            
    def edit_location(self, id, idtype, name, address, startjam, endjam, openjam, closejam, info):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE locations SET id_type = %s, name = %s, address = %s, best_at_start_hour = %s, best_at_end_hour = %s, open_at = %s, close_at = %s, information_url = %s, updated_at = %s  WHERE id = %s"
        try :
            cursor.execute(sql, 
                            (
                                idtype,
                                name,
                                address,
                                datetime.time(startjam).strftime("%I:00:00"),
                                datetime.time(endjam).strftime("%I:00:00"),
                                datetime.time(openjam).strftime("%I:00:00"),
                                datetime.time(closejam).strftime("%I:00:00"),
                                info,  
                                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                id
                            )
                        )
            print("Berhasil Update Database")
            self.connection.commit()
            return 0
        except :
            print("Tidak Berhasil Update Database")
            return 1

    def delete_location(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE locations SET status = %s, updated_at = %s  WHERE id = %s"
        cursor.execute(sql, ('DELETED', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), id))
        cursor.close()
        self.connection.commit()
        print("Berhasil Delete dari Database")    

    def close_connection(self):
        self.connection.close()
        

# ========================================================================================
# --------------------------------- Dependency Provider ----------------------------------
# ========================================================================================

class Database(DependencyProvider):

    connection_pool = None

    def __init__(self):
        print("DB Dependency Constructor")
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="database_pool",
                pool_size=5,
                pool_reset_session=True,
                host='127.0.0.1',
                database='traveller',
                user='root',
                password=''
            )
            print ("Success Connecting to MySQL")
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



