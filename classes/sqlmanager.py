import mysql.connector
from classes import system_postings

# This class provides the management and
# manipulation of all transactions made with the database.
class SQLManager:
    def __init__(self):
        self.db = 'payroll'
        self.user = 'root'
        self.passwd = ''
        self.conn = None
        self.cursor = None
        self.table = 'employees'
        self.table_atr = ['employee_name','employee_addr','jType','PayMethod','isInSyndicate']

    # This method is responsible for instantiating the connection to the database as an
    # object and instantiating our cursor, which will carry out the transactions.
    def databaseConn(self):
        try:
            self.conn = mysql.connector.connect(db=self.db, user=self.user, passwd=self.passwd, port=3307)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print("----------------------------")
            print("Failed to connect: {}".format(err))

    # This method is responsible for terminating the
    # connection object and removing the reference to the cursor.
    def databaseConnClose(self):
        try:
            self.cursor = None
            self.conn.close()
        except mysql.connector.Error as err:
            print("----------------------------")
            print("Failed to close connection: {}".format(err))

    # Method responsible for performing the insertion operation in a table
    # in our database, using the parameters specified in the class attributes and received from method call.
    def insertInTable(self, value):
        try:
            self.databaseConn()
            self.cursor.execute((
                "INSERT INTO employees (employee_name,employee_addr,jType,PayMethod,isInSyndicate,"
                "syndicateCharge, serviceCharge, wage, pointCardId, workedHours, sellCount)"
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            ), value)
            self.conn.commit()
            print("----------------------------")
            print("Successfully inserted")
        except mysql.connector.Error as err:
            print("----------------------------")
            print("Failed to insert in table: {}".format(err))
            self.conn.rollback()
        finally:
            self.databaseConnClose()
            print("----------------------------")
            print("Closed connection")

    # Method responsible for performing the remove operation on a table in our database, using the
    # parameters specified in the class attributes and received from the method call
    def deleteFromTable(self, value):
        try:
            self.databaseConn()
            self.cursor.execute((
                "DELETE * FROM employees WHERE employee_name = %s"
            ), (value,))
            self.conn.commit()
            print("----------------------------")
            print("Successfully removed")
        except mysql.connector.Error as err:
            print("----------------------------")
            print("Failed to delete from table: {}".format(err))
            self.conn.rollback()
        finally:
            self.databaseConnClose()
            print("----------------------------")
            print("Closed connection")

    # Method that updates an employee's record in our table
    # up_op is used to decide whether to change our employee's address or work type
    def updateTable(self, value, up_op):
        if up_op == 0:
            update_cmd = (
                "UPDATE employees SET employee_addr = %s WHERE employee_name = %s"
            )
        elif up_op == 1:
            update_cmd = (
                "UPDATE employees SET jType = %s WHERE employee_name = %s"
            )
        elif up_op == 2:
            update_cmd = (
                "UPDATE employees SET employee_name = %s WHERE employee_name = %s"
            )
        elif up_op == 3:
            update_cmd = (
                "UPDATE employees SET payMethod = %s WHERE employee_name = %s"
            )
        elif up_op == 4:
            update_cmd = (
                "UPDATE employees SET isInSyndicate = %s WHERE employee_name = %s"
            )
        elif up_op == 5:
            update_cmd = (
                "UPDATE employees SET syndicateCharge = %s WHERE employee_name = %s"
            )
        elif up_op == 6:
            update_cmd = (
                "UPDATE employees SET workedHours = %s WHERE employee_name = %s"
            )
        try:
            self.databaseConn()
            self.cursor.execute(update_cmd, value)
            self.conn.commit()
            print("----------------------------")
            print("Table updated successfully")
        except mysql.connector.Error as err:
            print("----------------------------")
            print("Failed to update table: {}".format(err))
        finally:
            self.databaseConnClose()
            print("----------------------------")
            print("Closed connection")

    # Method responsible for performing a name lookup in
    # our table, the method can be used to acquire information
    # about an employee to update reassemble the respective employee's class
    def searchInTable(self, value, type=None):
        result = None
        emplo = None
        if type == 1:
            emplo = system_postings.PointCard()
        elif type == 2:
            emplo = system_postings.SalePost()
        elif type == 3:
            pass

        try:
            self.databaseConn()
            print("aaaa")
            self.cursor.execute((
                "SELECT id, employee_name,employee_addr,jType,PayMethod,isInSyndicate,"
                "syndicateCharge,serviceCharge,wage,pointCardId,workedHours"
                " FROM employees WHERE employee_name = %s;"
            ), (value))

            result = self.cursor.fetchall()

            if type == 1:
                emplo.constructHourlyFSelect(result)
            elif type == 2:
                pass
            print(emplo.getEmployeeName())
            print("----------------------------")
            print("Search completed successfully")
        except mysql.connector.Error as err:
            print("----------------------------")
            print("Failed to search in table: {}".format(err))
        finally:
            self.databaseConnClose()
            print("----------------------------")
            print("Closed connection")
            return emplo
