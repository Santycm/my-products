import psycopg2
db_config = {'host':'localhost', 'user':'admin', 'password':'admin', 'database':'db_ferrer'}

class product:
    def __init__(self, description, price, stock) -> None:
        self.description = description
        self.price = price
        self.stock = stock

    def addToDB(self, iduser):
        try:
            connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
            cursor = connection.cursor()

            cursor.execute(f"call sp_insertproducts({iduser}, '{self.description}', {self.price}, {self.stock})")

            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()

def getProducts(iduser):
    try:
        connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
        cursor = connection.cursor()
        cursor.execute(f"SELECT idp, descriptionp, pricep, stockp FROM products where idu={iduser}")

        db_products = cursor.fetchall()

        return db_products
    except Exception as ex:
        print(ex)
    finally:
        connection.close()

def removeProduct(idproduct, iduser):
    try:
        connection = psycopg2.connect(host = db_config.get('host'),user = db_config.get('user'), password = db_config.get('password'), database = db_config.get('database'))
        cursor = connection.cursor()
        cursor.execute(f"call sp_DeleteProduct({idproduct}, {iduser})")
        connection.commit()
    except Exception as ex:
        print(ex)
    finally:
        connection.close()