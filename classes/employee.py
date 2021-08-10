from classes import sqlmanager
from sqlalchemy import Column, Integer, String, Boolean

jTypes = {"hourly": "hourly wage", "salaried": "monthly salary", "commissioned": "commission"}

# This class provides our mapping and planning for implementing and manipulating
# data and other functionality relating to our payroll employees.
class Employee(sqlmanager.Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    name = Column(String(55))
    address = Column(String(90))
    jType = Column(String(25))
    payMethod = Column(String(25))
    isInSyndicate = Column(Boolean)
    syndicateCharge = Column(String(10))
    serviceCharge = Column(String(10))
    wage = Column(String(10))
    pointCardId = Column(String(80))
    workedHours = Column(Integer)
    sellCount = Column(Integer)

    def __init__(self, id, name, address, jType, payMethod, isInSyndicate, syndicateCharge,
                 serviceCharge, wage, pointCardId, workedHours, sellCount):
        self.id = id
        self.name = name
        self.address = address
        self.jType = jType
        self.payMethod = payMethod
        self.isInSyndicate = isInSyndicate
        self.syndicateCharge = syndicateCharge
        self.serviceCharge = serviceCharge
        self.wage = wage
        self.pointCardId = pointCardId
        self.workedHours = workedHours
        self.sellCount = sellCount

class Hourly:
    def __init__(self, name=None, address=None, job_Type='hourly', syndicate=False):
        self.id = None
        self.name = name
        self.address = address
        self.jType = job_Type
        self.payMethod = jTypes[job_Type]
        self.isInSyndicate = syndicate
        self.syndicateCharge = None
        self.serviceCharge = None
        self.wage = None
        self.pointCardId = None
        self.workedHours = None

    # Method that returns our employee's name
    def getEmployeeName(self):
        return self.name

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getHourlyAttributes(self):
        return tuple(
            [self.name, self.address, self.jType, self.payMethod, self.isInSyndicate, self.syndicateCharge,
             self.serviceCharge, str(self.wage), self.pointCardId, self.workedHours, None]
        )

    # Method that constructs our class from the result of SELECT query in database
    def constructHourlyFSelect(self, SelectResult):
        self.id = SelectResult.id
        self.name = SelectResult.name
        self.address = SelectResult.address
        self.jType = SelectResult.jType
        self.payMethod = SelectResult.payMethod
        self.isInSyndicate = SelectResult.isInSyndicate
        self.syndicateCharge = SelectResult.syndicateCharge
        self.serviceCharge = SelectResult.serviceCharge
        self.wage = int(SelectResult.wage)
        self.pointCardId = SelectResult.pointCardId
        self.workedHours = SelectResult.workedHours


class Salaried:
    def __init__(self, name=None, address=None, job_Type='salaried', syndicate=False):
        self.name = name
        self.address = address
        self.jType = job_Type
        self.payMethod = jTypes[job_Type]
        self.isInSyndicate = syndicate
        self.syndicateCharge = None
        self.serviceCharge = None
        self.wage = None

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getSalariedAttributes(self):
        return tuple(
            [self.name, self.address, self.jType, self.payMethod, self.isInSyndicate,
             self.syndicateCharge, self.serviceCharge, self.wage, None, None, None]
        )


class Comissioned:
    def __init__(self, name=None, address=None, job_Type='commissioned', syndicate=False):
        self.id = None
        self.name = name
        self.address = address
        self.jType = job_Type
        self.payMethod = jTypes[job_Type]
        self.isInSyndicate = syndicate
        self.syndicateCharge = None
        self.serviceCharge = None
        self.wage = None
        self.saleDate = None
        self.salePrice = None
        self.saleId = None
        self.buyerName = None
        self.sellCount = 0

    # Method that returns our employee's name
    def getEmployeeName(self):
        return self.name

    # Method that updates our employee's sell counter
    def updateSellCount(self):
        self.sellCount += 1

    # Method that returns our employee's sell counter
    def getSellCount(self):
        return self.sellCount

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getComissionedAttributes(self):
        return tuple(
            [self.name, self.address, self.jType, self.payMethod, self.isInSyndicate,
             self.syndicateCharge, self.serviceCharge, self.wage, None, None, self.sellCount]
        )

    # Method that constructs our class from the result of SELECT query in database
    def constructCommsFSelect(self, SelectResult):
        self.id = SelectResult.id
        self.name = SelectResult.name
        self.address = SelectResult.address
        self.jType = SelectResult.jType
        self.payMethod = SelectResult.payMethod
        self.isInSyndicate = SelectResult.isInSyndicate
        self.syndicateCharge = SelectResult.syndicateCharge
        self.serviceCharge = SelectResult.serviceCharge
        self.wage = int(SelectResult.wage)
        self.sellCount = SelectResult.sellCount
        self.saleId = None
        self.saleDate = None
        self.salePrice = None
        self.buyerName = None