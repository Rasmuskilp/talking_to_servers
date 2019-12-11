from db_products_oop import *
from db_employees_oop import *
products_table = NWProducts()
employee_table =Employee_db()
while True:
    print('choose 1 for getting all products')
    print('choose 2 for getting 1 produdct')
    print('choose 3 for top 10')
    print('choose 4 for bottom 10')
    print('choose 5 for all employees')
    print('choose 6 for one employee')
    print('choose 7 if you want to search for employee by last name')
    user_i =input('Choose 1,2,3,4,5,6 pr 7')
    if user_i == '1':
        products_table.print_all()
        # print('getting all products')
    elif user_i == '2':
        id = products_table.set_id()
        products_table.read_one(id)
        print(products_table)
        # print('getting 1 product')
    elif user_i == '3':
        products_table.top_products()
        print(products_table)
    elif user_i == '4':
        products_table.bot_products()
        print(products_table)
    elif user_i == '5':
        employee_table.all_employee_data()
        print(employee_table)
    elif user_i == '6':
        id = employee_table.set_id()
        employee_table.one_employee_data()
        print(employee_table)
    elif user_i == '7':
        employee_table.search_employee()
        print(employee_table)
    elif 'bye' in user_i or 'exit' in user_i:
        print('goodbye! Thank you for choosing our programme.')
    else:
        print("I didn't quite get that, please choose from other available options.")




# table_products = NWProducts()
# products = NWProducts()
# product = NWProducts().read_one()
# products = products.read_all() # method real all - return something, but did not alter original variable
# products.fetchone()
# print(products.read_all)
# print(product.fetchone())