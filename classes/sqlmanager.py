import datetime
from sqlalchemy import create_engine, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, Date, Float
import datetime as dt

# MySQL connector defined
engine = create_engine("mysql+pymysql://user:password@localhost:port/database", echo=True)

# Define and create table
Base = declarative_base()

# Session for SQLALCHEMY's ORM
Session = sessionmaker(bind=engine)
session = Session()


class Syndicate(Base):
    __tablename__ = 'syndicate'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(55))
    address = Column(String(90))
    syndicateCharge = Column(Float)
    serviceCharge = Column(Float)

    def __init__(self, id, name, address, syndicateCharge, serviceCharge):
        self.id = id
        self.name = name
        self.address = address
        self.syndicateCharge = syndicateCharge
        self.serviceCharge = serviceCharge


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    saleId = Column(String(80))
    sellerName = Column(String(55))
    buyerName = Column(String(55))
    saleDate = Column(Date)
    salePrice = Column(Float)
    wasCommissioned = Column(Boolean)

    def __init__(self, saleId, sellerName, buyerName, saleDate, salePrice, wasCommissioned):
        self.saleId = saleId
        self.sellerName = sellerName
        self.buyerName = buyerName
        self.saleDate = saleDate
        self.salePrice = salePrice
        self.wasCommissioned = wasCommissioned


# This class provides our mapping and planning for implementing and manipulating
# data and other functionality relating to our payroll employees.
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(55))
    address = Column(String(90))
    jType = Column(String(25))
    payType = Column(String(25))
    payMethod = Column(Integer)
    isInSyndicate = Column(Boolean)
    syndicateCharge = Column(Float)
    serviceCharge = Column(Float)
    nextPayment = Column(Date)
    wage = Column(Float)
    pointCardId = Column(String(80))
    workedHours = Column(Integer)
    sellCount = Column(Integer)
    comissionPercent = Column(Float)

    def __init__(self, id, name, address, jType, payType, payMethod, isInSyndicate, syndicateCharge,
                 serviceCharge, nextPayment, wage, pointCardId, workedHours, sellCount, comissionPercent):
        self.id = id
        self.name = name
        self.address = address
        self.jType = jType
        self.payType = payType
        self.payMethod = payMethod
        self.isInSyndicate = isInSyndicate
        self.syndicateCharge = syndicateCharge
        self.serviceCharge = serviceCharge
        self.nextPayment = nextPayment
        self.wage = wage
        self.pointCardId = pointCardId
        self.workedHours = workedHours
        self.sellCount = sellCount
        self.comissionPercent = comissionPercent


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
            print("----------------------------")


    # Method responsible for performing the remove operation on a table in our database, using the
    # parameters specified in the class attributes and received from the method call
    def deleteFromTable(self, value):
        try:
            To_rmv = self.searchInTable(value, 0)

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
            print("----------------------------")

    # Method that updates an employee's record in our table
    # up_op is used to decide whether to change our employee's address or work type
    def updateTable(self, value, value2=None, up_op=None, date=None):
        try:
            if up_op == 0:
                hFunc = self.searchInTable(value, 0)
                hFunc.workedHours = value2

                session.commit()
            elif up_op == 1:
                sFunc = self.searchInTable(value, 0)
                sFunc.sellCount = value2

                session.commit()
            elif up_op == 2:
                chrgFunc = self.searchInTable(value, 0)
                chrgFunc.serviceCharge = value2

                session.commit()
            elif up_op == 3:
                addrFunc = self.searchInTable(value, 0)
                addrFunc.address = value2

                session.commit()
            elif up_op == 4:
                typFunc = self.searchInTable(value, 0)
                if value2.lower() == 'hourly':
                    typFunc.jType = value2
                    typFunc.payType = 'hourly wage'
                elif value2.lower() == 'commissioned':
                    typFunc.jType = value2
                    typFunc.payType = 'commission'
                else:
                    typFunc.jType = value2
                    typFunc.payType = 'monthly salary'
            elif up_op == 5:
                nnameFunc = self.searchInTable(value, 0)
                nnameFunc.name = value2

                session.commit()
            elif up_op == 6:
                Funct = self.searchInTable(value, 0)
                if Funct.jType.lower() == 'hourly':
                    Funct.nextPayment = date + dt.timedelta(7)
                    Funct.workedHours = 0
                    Funct.serviceCharge = 0
                    session.commit()
                elif Funct.jType.lower() == 'commissioned':
                    Funct.nextPayment = date + dt.timedelta(15)
                    Funct.sellCount = 0
                    Funct.serviceCharge = 0
                    session.commit()
                else:
                    Funct.nextPayment = date + dt.timedelta(30)
                    Funct.serviceCharge = 0
                    session.commit()

            print("----------------------------")
            print("Table updated successfully")
        except exc.SQLAlchemyError as err:
            print("----------------------------")
            print("Failed to update table: {}".format(err))
        finally:
            print("----------------------------")
            print("Closed connection")
            print("----------------------------")


    # Method responsible for performing a name lookup in
    # our tables, the method can be used to acquire information
    # about an employee to update reassemble the respective employee's class
    def searchInTable(self, value, opt):
        slct = None

        try:
            if opt == 0:
                slct = session.query(Employee).filter(Employee.name == value).first()
            elif opt == 1:
                query = session.query(Sales).filter(Sales.name == value).all()
                slct = 0
                for i in query:
                    slct += i.salePrice
                    i.wasCommissioned = True
                    session.commit()
            elif opt == 2:
                query = session.query(Employee).filter(Employee.payType == value).all()
                slct = []

                for c in query:
                    slct.append(c.name)

            elif opt == 3:
                query = session.query()

            print("----------------------------")
            print("Search completed successfully")
        except exc.SQLAlchemyError as err:
            print("----------------------------")
            print("Failed to search in table: {}".format(err))
        finally:
            print("----------------------------")
            print("Closed connection")
            print("----------------------------")
            return slct