import classes.system_postings, datetime
from classes import employee, sqlmanager

DbManager = sqlmanager.SQLManager()

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
        print("6 - Update employee record")
        print("4 - EXIT")
        print("----------------------------")
        x = int(input('Enter your option: '))
        if x == 1:
            name = input('Enter the employee\'s name: ')
            address = input('Enter the employee\'s address: ')
            print("----------------------------")
            print("----- Summary of jobs ------")
            print("---------- Hourly ----------")
            print("--------- Salaried ---------")
            print("------- Commissioned -------")
            print("----------------------------")
            j_type = input('Enter the employee\'s job: ')

            if j_type.lower() == 'hourly':
                New_Employee = employee.Hourly(name, address)
                DbManager.insertInTable(New_Employee.getHourlyAttributes())
            elif j_type.lower() == 'salaried':
                New_Employee = employee.Salaried(name, address)
                DbManager.insertInTable(New_Employee.getSalariedAttributes())
            elif j_type.lower() == 'commissioned':
                New_Employee = employee.Comissioned(name, address)
                DbManager.insertInTable(New_Employee.getComissionedAttributes())
        elif x == 2:
            name = input('Enter the name of the employee to be removed: ')
            DbManager.deleteFromTable(name)
        elif x == 3:
            name = input('Enter your name: ')
            Point_card = DbManager.searchInTable(name, 1)
            print(Point_card.getEmployeeName())
            arrival = int(input('Enter your time of entry: '))
            departure = int(input('Enter your departure time: '))
            DbManager.updateTable(Point_card.postPointCard(arrival,departure), 6)
        elif x == 4:
            name = input('Enter your name: ')
            New_sale = DbManager.searchInTable(name, 2)
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