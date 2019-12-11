import pyodbc
from db_connect_oop import *
class NWProducts(MSDBConnection):
    def __sql_query(self, sql_query):  # Makes it private
        return self.cursor.execute(sql_query)

    def read_all(self):
        # build our SQL query
        query = 'SELECT * FROM Products'
        # execute our query
        data = self.__sql_query(query)
        # data = super().__sql_query(query)
        return data
        # return an iteratable object
    def set_id(self):
        id = int(input('select an id'))
        return id
    def read_one(self, id):
        # id = self.set_id()
        query2 = f'SELECT * FROM Products WHERE ProductID = {int(id)}'
        item = self.__sql_query(query2)
        record = item.fetchone()
        # if item is None:
        #     exit()
        # return(f"{item.ProductID} - {item.ProductName} £{item.UnitPrice}")
        # while True:
        #     print(products.fetchone())
        print(record)
        #print all products using the while loop and fetchone()
    def print_all(self):
        query = 'SELECT * FROM Products'
        data = self.__sql_query(query)
        while True:
            record = data.fetchone()
            if record is None:
                break
            print(f"{record.ProductID} - {record.ProductName} £{record.UnitPrice}")
    #gets(prints) top 10 products by price - Formatted
    def top_products(self):
        query3 ='SELECT TOP 10 * FROM Products ORDER BY UnitPrice desc'
        data = self.__sql_query(query3)
        print( data.fetchall())
    # gets(prints) bottom 10 products by price - Formated
    def bot_products(self):
        query4 = 'SELECT TOP 10 * FROM Products ORDER BY UnitPrice asc'
        data = self.__sql_query(query4)
        print( data.fetchall())
    def average(self):
        query = 'SELECT AVG(UnitPrice) FROM Products'
        data = self.__sql_query(query)
        print( data.fetchall())
    def max(self):
        query = 'SELECT Max(UnitPrice) FROM Products'
        data = self.__sql_query(query)
        print( data.fetchall())
    def min(self):
        query = 'SELECT MIN(UnitPrice) FROM Products'
        data = self.__sql_query(query)
        print( data.fetchall())
    def range(self):
        lower = input('Enter lower bound for range')
        upper = input('Enter upper bound for range')
        query = f'SELECT * FROM Products WHERE UnitPrice BETWEEN {lower} AND {upper}'
        data = self.__sql_query(query)
        print( data.fetchall())
    def name_search(self):
        name = input('Enter the product name')
        query = f'SELECT * FROM Products where ProductName = {name}'
        data = self.__sql_query(query)
        print( data.fetchall())
    def create(self):
        name_create = input('Enter the product name which you want to create')
        query = f'Insert into Products (ProductName) VALUES ({name_create})'
        query2 = f'SELECT * FROM Products WHERE ProductName = {name_create}'
        data = self.__sql_query(query)
        data2 = self.__sql_query(query2)
        print( data2.fetchall())
    #Search product by name

#variable for NW Product table
# table_products = NWProducts()
# products = NWProducts()
# product = NWProducts().read_one()
# products = products.read_all() # method real all - return something, but did not alter original variable
# products.fetchone()
# print(products.read_all)
# print(product.fetchone())
    # Read / list all
    # Read one
    ## ask for input --> front end -- input()

    # create one --> makes things persistent in DB
    # update one
    # destroy one
    #