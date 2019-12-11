#get all employees data
# get one employee by id
# search for one employee by name or last_name
## Add all these amazing functionality to our own run_products while loop
from db_connect_oop import *
class Employee_db(MSDBConnection):
    def __sql_query(self, sql_query):  # Makes it private
        return self.cursor.execute(sql_query)
    def all_employee_data(self):
        query = 'SELECT * FROM Employees'
        data = self.__sql_query(query)
        print( data.fetchall())
    def set_id(self):
        id = int(input('insert your id:'))
        return id
    def one_employee_data(self):
        id = self.set_id()
        query2 = f'SELECT * FROM Employees WHERE EmployeeID = {int(id)}'
        item = self.__sql_query(query2)
        record = item.fetchone()
        # if item is None:
        #     exit()
        # return(f"{item.ProductID} - {item.ProductName} £{item.UnitPrice}")
        # while True:
        #     print(products.fetchone())
        print( record)

    def search_employee(self):
        employee_last_name = str(input('tell me the last name you want to search for'))
        query = (f'SELECT * FROM Employees WHERE LastName = { employee_last_name}')
        item = self.__sql_query(query)
        record = item.fetchone()
        print( record)

