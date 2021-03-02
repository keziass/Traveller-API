from nameko.extensions import DependencyProvider

import mysql.connector # pip install mysql-connector-python
from mysql.connector import Error
from mysql.connector import pooling

# ========================================================================================
# ----------------------------------- Database Wrapper -----------------------------------
# ========================================================================================

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection
    
    def get_all_travelplan(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM travel_plans"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_user': row['id_user'],
                'name': row['name'],
                'number_of_people': row['number_of_people'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_travelplan_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM travel_plans WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_travelplan_by_userID(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM travel_plans WHERE id_user = {}".format(id)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_user': row['id_user'],
                'name': row['name'],
                'number_of_people': row['number_of_people'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def search_travelplan(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM travel_plans WHERE id = %s AND id_user = %s AND name = %s AND number_of_people = %s AND status = %s"
        cursor.execute(sql,
                            (
                                data['id'],
                                data['id_user'],
                                data['name'],
                                data['number_of_people'],
                                data['status']
                            )
                    )
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def get_last_travelplan(self):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM travel_plans ORDER BY id DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_all_detail_travelplan(self):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM travel_plan_details"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_travel_plan': row['id_travel_plan'],
                'id_ref_location': row['id_ref_location'],
                'id_ref_hotel': row['id_ref_hotel'],
                'day': row['day'],
                'start_hour': row['start_hour'],
                'end_hour': row['end_hour'],
                'description': row['description'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result
    
    def get_detail_travelplan_by_id(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM travel_plan_details WHERE id = {}".format(id)
        cursor.execute(sql)
        result = cursor.fetchone()
        cursor.close()
        return result

    def get_detail_travelplan_by_travelplanID(self, id):
        cursor = self.connection.cursor(dictionary=True)
        result = []
        sql = "SELECT * FROM travel_plan_details WHERE id_travel_plan = {}".format(id)
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'id_travel_plan': row['id_travel_plan'],
                'id_ref_location': row['id_ref_location'],
                'id_ref_hotel': row['id_ref_hotel'],
                'day': row['day'],
                'start_hour': row['start_hour'],
                'end_hour': row['end_hour'],
                'description': row['description'],
                'status': row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def search_detail_travelplan(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM travel_plan_details WHERE id = %s AND id_travel_plan = %s AND id_ref_location = %s AND id_ref_hotel = %s AND day = %s AND start_hour = %s AND end_hour = %s AND description = %s AND status = %s"
        cursor.execute(sql,
                            (
                                data['id'],
                                data['id_travel_plan'],
                                data['id_ref_location'],
                                data['id_ref_hotel'],
                                data['day'],
                                data['start_hour'],
                                data['end_hour'],
                                data['description'],
                                data['status']
                            )
                    )
        result = cursor.fetchone()
        cursor.close()
        return result

    def create_travelplan(self, id_user, name, number_of_people):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO travel_plans VALUES(default, %s, %s, %s, 'ACTIVE_PUBLIC', default, default)"
        cursor.execute(sql,(id_user,name,number_of_people))
        self.connection.commit()
    
    def create_detailtravelplan(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "INSERT INTO travel_plan_details VALUES(default, %s, %s, %s, %s, %s, %s, %s, 'ACTIVE', default, default)"
        cursor.execute(sql,
                            (
                                data['id_travel_plan'],
                                data['id_ref_location'],
                                data['id_ref_hotel'],
                                data['day'],
                                data['start_hour'],
                                data['end_hour'],
                                data['description']
                            )
                    )
        self.connection.commit()
    
    def cancel_travelplan(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE travel_plans SET status = 'CANCELED' WHERE id = {}".format(id)
        cursor.execute(sql,(id))
        cursor.close()
        self.connection.commit()
    
    def cancel_detailtravelplan(self, id):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE travel_plan_details SET status = 'CANCELED' WHERE id = {}".format(id)
        cursor.execute(sql,(id))
        cursor.close()
        self.connection.commit()
    
    def edit_travelplan(self, id, id_user, name, number_of_people):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE travel_plans SET id_user = %s, name = %s, number_of_people = %s, updated_at=default WHERE id = %s"
        cursor.execute(sql,(id_user,name,number_of_people,id))
        cursor.close()
        self.connection.commit()
    
    def edit_detailtravelplan(self, data):
        cursor = self.connection.cursor(dictionary=True)
        sql = "UPDATE travel_plan_details SET id_travel_plan = %s, id_ref_location = %s, id_ref_hotel = %s, day = %s, start_hour = %s, end_hour = %s, description = %s, updated_at=default WHERE id = %s"
        cursor.execute(sql,
                            (
                                data['id_travel_plan'],
                                data['id_ref_location'],
                                data['id_ref_hotel'],
                                data['day'],
                                data['start_hour'],
                                data['end_hour'],
                                data['description'],
                                data['id']
                            )
                    )
        cursor.close()
        self.connection.commit()

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
                pool_size=3,
                pool_reset_session=True,
                host='127.0.0.1',
                database='traveller',
                user='root',
                password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



