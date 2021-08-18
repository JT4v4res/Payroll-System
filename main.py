import datetime

from classes import sqlmanager, system_postings
import uuid
import datetime as dt

DbManager = sqlmanager.SQLManager()

sqlmanager.Base.metadata.create_all(sqlmanager.engine)

if __name__ == '__main__':
    while True:
        print("Welcome to Payroll System")
        print("Please, select an action")
        print("----------------------------")
        print("1 - Add a new employee")
        print("2 - Remove an employee")
        print("3 - Beat time")
        print("4 - Launch new sale")
        print("5 - Launch service charge")
        print("6 - Update employee record")
        print("7 - Make today\'s payments")
        print("8 - Personalized schedules")
        print("11 - EXIT")
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
            tax = 0
            if isInSyndicate:
                tax = input('Enter the syndicate charge: ')
                DbManager.insertInTable(
                    sqlmanager.Syndicate(
                        None, name, address, tax, 0
                    )
                )

            payMethod = input('Choose your paymethod between: \n 1.Check by mail\n 2.Check in hand\n 3.Account deposit\n opt:')

            if j_type.lower() == 'hourly':
                DbManager.insertInTable(
                    sqlmanager.Employee(
                        None, name, address, j_type, 'hourly wage', payMethod, isInSyndicate, tax,
                        0, dt.date.today() + dt.timedelta(7), wage, str(uuid.uuid4()), 0, None, None
                    )
                )
            elif j_type.lower() == 'salaried':
                DbManager.insertInTable(
                    sqlmanager.Employee(
                        None, name, address, j_type, 'monthly salary', payMethod, isInSyndicate, tax,
                        0, dt.date.today() + dt.timedelta(30), wage, None, None, None, None
                    )
                )
            elif j_type.lower() == 'commissioned':
                percentComm = input('Enter the percentual of commission: ')

                DbManager.insertInTable(
                    sqlmanager.Employee(
                        None, name, address, j_type, 'commission', payMethod, isInSyndicate, tax,
                        0, dt.date.today() + dt.timedelta(15), wage, None, None, 0, percentComm
                    )
                )
        elif x == 2:
            name = input('Enter the name of the employee to be removed: ')
            DbManager.deleteFromTable(name, 1)
        elif x == 3:
            name = input('Enter your name: ')
            Point_card = system_postings.PointCard()
            Point_card.constructHourlyFSelect(DbManager.searchInTable(name, 0))

            arrival = int(input('Enter your time of entry: '))
            departure = int(input('Enter your departure time: '))

            DbManager.updateTable(Point_card.getEmployeeName(), Point_card.postPointCard(arrival, departure), 0)
        elif x == 4:
            name = input('Enter your name: ')
            New_sale = system_postings.SalePost()
            New_sale.constructCommsFSelect(DbManager.searchInTable(name, 0))

            bName = input('Buyer name: ')
            price = input('Sell price: ')

            New_sale.getSale(bName, price)
            sTup = New_sale.postNewSale()

            DbManager.updateTable(New_sale.getEmployeeName(), New_sale.getSellCount(), 1)
            DbManager.insertInTable(
                sqlmanager.Sales(sTup[0], sTup[1], sTup[2],
                                      sTup[3], sTup[4], None)
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
                DbManager.updateTable(e_name, n_addr, 3)
            elif y == 2:
                n_type = input('Enter new type: ')
                DbManager.updateTable(e_name, n_type, 4)
            elif y == 3:
                n_name = input('Enter new name: ')
                DbManager.updateTable(e_name, n_name, 5)
            elif y == 4:
                n_syndicate = input('Syndicate True or False: ')
                name = input('Enter your name: ')
                if n_syndicate.lower() == 'true':
                    address = input('Enter you address: ')
                    tax = input('Enter tax: ')
                    DbManager.insertInTable(
                        sqlmanager.Syndicate(
                            None, name, address, tax, 0
                        )
                    )
                else:
                    DbManager.deleteFromTable(name, 2)
            elif y == 5:
                charge = input('Enter syndicate charge: ')
                DbManager.updateTable(e_name, charge, 7)
            elif y == 6:
                print('------------------------')
                print("Table of week days")
                print("0 - Monday")
                print("1 - Tuesday")
                print("2 - Wednessday")
                print("3 - Thursday")
                print("4 - Friday")
                print('------------------------')
                name = input('Enter your name: ')
                dCode = int(input('Enter the day of payment on schedule: '))
                newPaySched = input('Enter the new payment schedule description: ').lower()
                DbManager.insertInTable(
                    sqlmanager.PersoSchedule(None, dCode, newPaySched)
                )
                if newPaySched == 'monday':
                    DbManager.updateTable(name, 'monday', 8)
                elif newPaySched == 'tuesday':
                    DbManager.updateTable(name, 'tuesday', 8)
                elif newPaySched == 'wednessday':
                    DbManager.updateTable(name, 'wednessday', 8)
                elif newPaySched == 'thursday':
                    DbManager.updateTable(name, 'thursday', 8)
                elif newPaySched == 'friday':
                    DbManager.updateTable(name, 'friday', 8)
        elif x == 7:
            print('------------------------')
            print('1.Pay today\'s employees')
            print('2.Pay in a given period')
            print('------------------------')

            z = int(input('option: '))
            if z == 1:
                paymnt = system_postings.PaymentSchedule()
                paymnt.payWeekly()
                paymnt.pay2Weekly()
                paymnt.payMonthly()
            else:
                days = int(input('Enter period: '))
                paymnt = system_postings.PaymentSchedule()
                paymnt.payWeekly(days)
                paymnt.pay2Weekly(days)
                paymnt.payMonthly(days)
                paymnt.PersoPayment(days)
        elif x == 8:
            print('------------------------')
            print("Table of week days")
            print("0 - Monday")
            print("1 - Tuesday")
            print("2 - Wednessday")
            print("3 - Thursday")
            print("4 - Friday")
            print('------------------------')
            name = input('Enter your name: ')
            dCode = int(input('Enter the day of payment on schedule: '))
            newPaySched = input('Enter the new payment schedule description: ').lower()
            DbManager.insertInTable(
                sqlmanager.PersoSchedule(None, dCode, newPaySched)
            )
            if newPaySched == 'monday':
                DbManager.updateTable(name, 'monday', 8)
            elif newPaySched == 'tuesday':
                DbManager.updateTable(name, 'tuesday', 8)
            elif newPaySched == 'wednessday':
                DbManager.updateTable(name, 'wednessday', 8)
            elif newPaySched == 'thursday':
                DbManager.updateTable(name, 'thursday', 8)
            elif newPaySched == 'friday':
                DbManager.updateTable(name, 'friday', 8)
        else:
            break