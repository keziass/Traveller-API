from nameko.extensions import DependencyProvider
import pymysqlpool
import pymysql

class DatabaseWrapper:

    connection = None

    def __init__(self, connection):
        print("DB Wrapper Constructor")
        self.connection = connection

    def log_in(self, email, password):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(sql, args=(email, password))

        res = {
            'err': 0,
            'msg': '',
            'data': {}
        }

        if cursor.rowcount > 0:
            res['data'] = cursor.fetchone()
            res['msg'] = 'Success'
            res['err'] = 0
        else:
            res['err'] = 1
            res['msg'] = 'Error: User not Found'
        return res
    
    def create_user(self, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querysql = "INSERT INTO users VALUES(default,%s, %s, %s, %s, %s, %s, 'ACTIVE')"
        cursor.execute(querysql, 
                        (
                            data['email'], 
                            data['password'], 
                            data['name'], 
                            data['gender'], 
                            data['dob'], 
                            data['address']
                        )
                    )
        self.connection.commit()
    
    def get_user_by_id(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querysql = "SELECT * FROM users WHERE id = {} and status= 'ACTIVE'".format(id)
        cursor.execute(querysql)
        results = cursor.fetchone()
        cursor.close()
        return results

    def delete_user(self, id):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querysql = "UPDATE users SET status = 'DELETED' WHERE id = %s" 
        cursor.execute(querysql, (id))
        cursor.close()
        self.connection.commit()

    def get_all_active_user(self):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        result = []
        sql = "SELECT * FROM users WHERE status = 'ACTIVE';"
        cursor.execute(sql)
        for row in cursor.fetchall():
            result.append({
                'id': row['id'],
                'email': row['email'],
                'password': row['password'],
                'name': row['name'],
                'gender': row['gender'],
                'dob': row['dob'],
                'address': row['address'],
                'status':row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })
        cursor.close()
        return result

    def search_user(self, name):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querysql = "SELECT * FROM users WHERE name LIKE '%{}%' AND status = 'ACTIVE'".format(name)
        cursor.execute(querysql)
        results = []

        for row in cursor.fetchall():
            results.append({
                'id': row['id'],
                'email': row['email'],
                'password': row['password'],
                'name': row['name'],
                'gender': row['gender'],
                'dob': row['dob'],
                'address': row['address'],
                'status':row['status'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
            })

        cursor.close()
        return results

    def edit_user(self, id, data):
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        querySql = "UPDATE users SET name = %s, email = %s, address = %s, star = %s WHERE id = %s "
        cursor.execute(querySql, (
            data['email'], 
            data['password'], 
            data['name'], 
            data['gender'], 
            data['dob'], 
            data['address'],
            id
        ))
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
        config={'host':'127.0.0.1', 'user':'root', 'password':'', 'database':'traveller', 'autocommit':True}
        self.connection_pool = pymysqlpool.ConnectionPool(size=5, name='DB Pool', **config)
    
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
    
    def __del__(self):
        print("DB Dependency Destructor")
    
    



