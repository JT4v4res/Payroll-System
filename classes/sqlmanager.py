import mysql.connector
import sqlalchemy
from classes import employee
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQL connector defined
engine = create_engine("mysql+pymysql://root:Terumis2-@localhost:3307/payroll", echo=True)

# Define and create table
Base = declarative_base()

# Session for SQLALCHEMY's ORM
Session = sessionmaker(bind=engine)
session = Session()

# This class provides the management and
# manipulation of all transactions made with the database.
class SQLManager:
    pass

    # Method responsible for performing the insertion operation in a table
    # in our database, using the parameters specified in the class attributes and received from method call.
    def insertInTable(self, value):
        try:
            session.add(value)
            session.commit()

            print("----------------------------")
            print("Successfully inserted")
        except exc.SQLAlchemyError as err:
            print("----------------------------")
            print("Failed to insert in table: {}".format(err))
        finally:
            print("----------------------------")
            print("Closed connection")

    # Method responsible for performing the remove operation on a table in our database, using the
    # parameters specified in the class attributes and received from the method call
    def deleteFromTable(self, value):
        try:
            To_rmv = self.searchInTable(value)

            session.delete(To_rmv)
            session.commit()
            print("----------------------------")
            print("Successfully removed")
        except exc.SQLAlchemyError as err:
            print("----------------------------")
            print("Failed to delete from table: {}".format(err))
        finally:
            print("----------------------------")
            print("Closed connection")

    # Method that updates an employee's record in our table
    # up_op is used to decide whether to change our employee's address or work type
    def updateTable(self, value, value2, up_op):
        try:
            if up_op == 0:
                hFunc = self.searchInTable(value)
                hFunc.workedHours = value2

                session.commit()
            elif up_op == 1:
                sFunc = self.searchInTable(value)
                sFunc.sellCount = value2

                session.commit()
            elif up_op == 2:
                chrgFunc = self.searchInTable(value)
                chrgFunc.serviceCharge = value2

                session.commit()

            print("----------------------------")
            print("Table updated successfully")
        except exc.SQLAlchemyError as err:
            print("----------------------------")
            print("Failed to update table: {}".format(err))
        finally:
            print("----------------------------")
            print("Closed connection")

    # Method responsible for performing a name lookup in
    # our table, the method can be used to acquire information
    # about an employee to update reassemble the respective employee's class
    def searchInTable(self, value):
        slct = None

        try:
            slct = session.query(employee.Employee).filter(employee.Employee.name == value).first()

            print("----------------------------")
            print("Search completed successfully")
        except exc.SQLAlchemyError as err:
            print("----------------------------")
            print("Failed to search in table: {}".format(err))
        finally:
            print("----------------------------")
            print("Closed connection")
            return slct