import pyodbc
from db_connect_oop import *
class NWProducts(MSDBConnection):
    def read_all(self):
        # build our SQL query
        query = 'SELECT * FROM Products'
        # execute our query
        data = super().__sql_query(query)
        return data
        # return an iteratable object
    products = NWProducts().read_all
    print(products.fetchone())
    # Read / list all
    # Read one
    ## ask for input --> front end -- input()

    # create one --> makes things persistent in DB
    # update one
    # destroy one
    #