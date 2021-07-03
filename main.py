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
        print("3 - EXIT")
        print("----------------------------")
        x = int(input('Enter your option: '))
        if x == 1:
            name = input('Enter the employee\'s name: ')
            address = input('Enter the employee\'s address: ')
            print("----------------------------")
            print("--- Summary of job types ---")
            print("---------- Hourly ----------")
            print("--------- Salaried ---------")
            print("------- Commissioned -------")
            print("----------------------------")
            j_type = input('Enter the employee\'s job: ')
            New_Employee = employee.Employee(name, address, j_type)
            DbManager.insertInTable(New_Employee.getEmployeeAttributes())
        elif x == 2:
            name = input('Enter the name of the employee to be removed: ')
            DbManager.deleteFromTable(name)
        else:
            break