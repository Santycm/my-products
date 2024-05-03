import psycopg2

db_config = {'host':'localhost', 'user':'admin', 'password':'admin', 'database':'db_ferrer'}
class user:
    def __init__(self, name, lastname, telephone, email, password):
        self.name = name
        self.lastname = lastname
        self.telephone = telephone
        self.email = email
        self.password = password

    def addToDB(self, userA):
        try:
            connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
            cursor = connection.cursor()

            cursor.execute(f"call sp_insertusers('{self.name}', '{self.lastname}', '{self.telephone}', '{self.email}', '{userA}', '{self.password}')")

            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()

    def AssignUser(self):
        for i in range(len(self.email)):
            if self.email[i] == "@":
                return self.email[:i]
            
    def regUser(self):
        Exists = False
        userA = self.AssignUser()

        try:
            connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
            cursor = connection.cursor()
            cursor.execute("SELECT usera, passa FROM userA")

            users = cursor.fetchall()
            for user in users:
                if user[0] == userA:
                    Exists = True
                    break
                else:
                    Exists = False

            if Exists:
                return False
            else:
                self.addToDB(userA)
                return True
                
        except Exception as ex:
            print(ex)
        finally:
            connection.close()     

def authUser(user, password):
    try:
        connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
        cursor = connection.cursor()
        cursor.execute("SELECT usera, passa FROM userA")

        db_users= cursor.fetchall()

        Correct = False
        for user_db in db_users:
            if user_db[0] == user and user_db[1] == password:
                Correct = True
                break
            else:
                Correct = False

        return Correct
    except Exception as ex:
        print(ex)
    finally:
        connection.close()

def getNameUser(user):
    try:
        connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
        cursor = connection.cursor()
        cursor.execute("SELECT usera, nameu, lastnu FROM userA")

        db_users= cursor.fetchall()

        for user_db in db_users:
            if user_db[0] == user:
                return f"{user_db[1]} {user_db[2]}"
    except Exception as ex:
        print(ex)
    finally:
        connection.close()

def getIDUser(user):
    try:
        connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
        cursor = connection.cursor()
        cursor.execute(f"SELECT idu FROM userA where usera='{user}'")

        db_users= cursor.fetchall()

        for user_db in db_users:
            return user_db[0]
    except Exception as ex:
        print(ex)
    finally:
        connection.close()  
