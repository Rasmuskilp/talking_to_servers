import pyodbc
#these are our Variables to connect
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
#Making the connection
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#This is making a cursor
cursor = docker_Northwind.cursor()
#executing some SQL commands
cursor.execute("SELECT * FROM Customers WHERE city LIKE 'London'")
# Cursor will maintain state
#Fetching data from the executed SQL command and printing
#
row = cursor.fetchone()
# print(row)
#.fetchone() method
#Cursor maintaing state
# print(cursor.fetchone())
# print(cursor.fetchone())
#Accessing specific data or column
    #use the column name as an attribute of the entry
# row = cursor.fetchone()
# print(row)
# print(row.CompanyName,row.ContactName)
#fetchall  - bad practice
rows_all = cursor.fetchall()
print(rows_all)
print(len(rows_all))
print(type(rows_all))
for line in rows_all:
    print(line.ContactName, line.CompanyName,line.Fax)
# to get lots of data - use a while loop and fetchone at a time
rows = cursor.execute("SELECT * FROM Products")
while True:
    record = rows.fetchone()
    if record is None :
        break
    else:
        print(record.UnitPrice)