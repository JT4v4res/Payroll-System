from classes import employee, sqlmanager, system_postings
import uuid

DbManager = sqlmanager.SQLManager()

sqlmanager.Base.metadata.create_all(sqlmanager.engine)

if __name__ == '__main__':
    while True:
        print("----------------------------")
        print("Welcome to Payroll System")
        print("Please, select an action")
        print("----------------------------")
        print("1 - Add a new employee")
        print("2 - Remove an employee")
        print("3 - Beat time")
        print("4 - Launch new sale")
        print("5 - Launch Service Charge")
        print("6 - Update employee record")
        print("7 - EXIT")
        print("----------------------------")
        x = int(input('Enter your option: '))
        if x == 1:
            name = input('Enter the employee\'s name: ')
            address = input('Enter the employee\'s address: ')
            isInSyndicate = input('Syndicate: True or False: ')
            if isInSyndicate.lower() == 'true':
                isInSyndicate = True
            else:
                isInSyndicate = False
            wage = input('Employee\'s wage: ')
            print("----------------------------")
            print("----- Summary of jobs ------")
            print("---------- Hourly ----------")
            print("--------- Salaried ---------")
            print("------- Commissioned -------")
            print("----------------------------")
            j_type = input('Enter the employee\'s job: ')

            if j_type.lower() == 'hourly':
                DbManager.insertInTable(
                    employee.Employee(
                        None,name,address,j_type,'hourly wage', isInSyndicate, None,
                        None, wage, str(uuid.uuid4()), 0, None
                    )
                )
            elif j_type.lower() == 'salaried':
                DbManager.insertInTable(
                    employee.Employee(
                        None, name, address, j_type, 'monthly salary', isInSyndicate, None,
                        None, wage, None, None, None
                    )
                )
            elif j_type.lower() == 'commissioned':
                DbManager.insertInTable(
                    employee.Employee(
                        None, name, address, j_type, 'commission', isInSyndicate, None,
                        None, wage, None, None, 0
                    )
                )
        elif x == 2:
            name = input('Enter the name of the employee to be removed: ')
            DbManager.deleteFromTable(name)
        elif x == 3:
            name = input('Enter your name: ')
            Point_card = system_postings.PointCard()
            Point_card.constructHourlyFSelect(DbManager.searchInTable(name))

            arrival = int(input('Enter your time of entry: '))
            departure = int(input('Enter your departure time: '))

            DbManager.updateTable(Point_card.getEmployeeName(), Point_card.postPointCard(arrival, departure), 0)
        elif x == 4:
            name = input('Enter your name: ')
            New_sale = system_postings.SalePost()
            New_sale.constructCommsFSelect(DbManager.searchInTable(name))

            bName = input('Buyer name: ')
            price = input('Sell price: ')

            New_sale.getSale(bName, price)
            sTup = New_sale.postNewSale()

            DbManager.updateTable(New_sale.getEmployeeName(), New_sale.getSellCount(), 1)
            DbManager.insertInTable(
                system_postings.Sales(sTup[0], sTup[1], sTup[2],
                                      sTup[3], sTup[4])
            )
        elif x == 5:
            name = input('Enter employee\'s name: ')
            charge = input('Enter the service charge: ')

            DbManager.updateTable(name, charge, 2)
        elif x == 6:
            e_name = input('Enter your name: ')
            print("----------------------------")
            print("---- Summary of Updates ----")
            print("------- 1 - Address  -------")
            print("--------- 2 - Type ---------")
            print("--------- 3 - Name ---------")
            print("------ 4 - Syndicate -------")
            print("--- 5 - Syndicate Charge ---")
            print("---- 6 - Payment method ----")
            print("----------------------------")
            y = int(input('Enter option: '))
            if y == 1:
                n_addr = input('Enter new address: ')
                DbManager.updateTable(tuple(n_addr,e_name),0)
            elif y == 2:
                n_type = input('Enter new type: ')
                DbManager.updateTable(tuple(n_type,e_name),1)
            elif y == 3:
                n_name = input('Enter new name: ')
                DbManager.updateTable(tuple(n_name,e_name),2)
            elif y == 4:
                n_syndicate = input('Syndicate True or False: ')
                DbManager.updateTable(tuple(n_syndicate,e_name),4)
            elif y == 5:
                charge = input('Enter syndicate charge: ')
                DbManager.updateTable(tuple(charge,e_name),5)
            elif y == 6:
                n_pMethod = input('Enter new payment method: ')
                DbManager.updateTable(tuple(n_pMethod,e_name),3)
        else:
            break