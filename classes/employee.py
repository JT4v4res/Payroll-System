from classes import sqlmanager

jTypes = {"hourly": "hourly wage", "salaried": "monthly salary", "commissioned": "commission"}


class Hourly:
    def __init__(self, name=None, address=None, payMethod=None,job_Type='hourly', syndicate=False):
        self.id = None
        self.name = name
        self.address = address
        self.jType = job_Type
        self.payType = jTypes[job_Type]
        self.payMethod = payMethod
        self.isInSyndicate = syndicate
        self.syndicateCharge = None
        self.serviceCharge = None
        self.nextPayment = None
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
            [self.name, self.address, self.jType, self.payType, self.payMethod, self.isInSyndicate, self.syndicateCharge,
             self.serviceCharge, self.nextPayment, str(self.wage), self.pointCardId, self.workedHours, None]
        )

    def getExtraWorkHours(self):
        extra = 56 - (self.workedHours / 7)
        if extra > 0:
            return 0
        else:
            return extra * (-1)

    # Method that constructs our class from the result of SELECT query in database
    def constructHourlyFSelect(self, SelectResult):
        self.id = SelectResult.id
        self.name = SelectResult.name
        self.address = SelectResult.address
        self.jType = SelectResult.jType
        self.payType = SelectResult.payType
        self.payMethod = SelectResult.payMethod
        self.isInSyndicate = SelectResult.isInSyndicate
        self.syndicateCharge = SelectResult.syndicateCharge
        self.serviceCharge = SelectResult.serviceCharge
        self.nextPayment = SelectResult.nextPayment
        self.wage = int(SelectResult.wage)
        self.pointCardId = SelectResult.pointCardId
        self.workedHours = SelectResult.workedHours


class Salaried:
    def __init__(self, name=None, address=None, payMethod=None, job_Type='salaried', syndicate=False):
        self.id = None
        self.name = name
        self.address = address
        self.jType = job_Type
        self.payType = jTypes[job_Type]
        self.payMethod = payMethod
        self.isInSyndicate = syndicate
        self.syndicateCharge = None
        self.serviceCharge = None
        self.nextPayment = None
        self.wage = None

    # Method that returns our employee's name
    def getEmployeeName(self):
        return self.name

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getSalariedAttributes(self):
        return tuple(
            [self.name, self.address, self.jType, self.payMethod, self.isInSyndicate,
             self.syndicateCharge, self.serviceCharge, self.nextPayment, self.wage, None, None, None]
        )

    # Method that constructs our class from the result of SELECT query in database
    def constructSalFSelect(self, SelectResult):
        self.id = SelectResult.id
        self.name = SelectResult.name
        self.address = SelectResult.address
        self.jType = SelectResult.jType
        self.payType = SelectResult.payType
        self.payMethod = SelectResult.payMethod
        self.isInSyndicate = SelectResult.isInSyndicate
        self.syndicateCharge = SelectResult.syndicateCharge
        self.serviceCharge = SelectResult.serviceCharge
        self.nextPayment = SelectResult.nextPayment
        self.wage = int(SelectResult.wage)



class Comissioned:
    def __init__(self, name=None, address=None, payMethod=None, job_Type='commissioned', syndicate=False):
        self.id = None
        self.name = name
        self.address = address
        self.jType = job_Type
        self.payType = jTypes[job_Type]
        self.payMethod = payMethod
        self.isInSyndicate = syndicate
        self.syndicateCharge = None
        self.serviceCharge = None
        self.nextPayment = None
        self.wage = None
        self.saleDate = None
        self.salePrice = None
        self.saleId = None
        self.buyerName = None
        self.sellCount = 0
        self.comissionPercent = None

    # Method that returns our employee's name
    def getEmployeeName(self):
        return self.name

    # Method that updates our employee's sell counter
    def updateSellCount(self):
        self.sellCount += 1

    # Method that returns our employee's sell counter
    def getSellCount(self):
        return self.sellCount

    # Method that takes the total sales amount of the commissionee to calculate
    # the commission rate and calculate the employee's total payment
    def getPayment(self, name):
        TempMGR = sqlmanager.SQLManager()

        totalSells = TempMGR.searchInTable(name, 1)

        if totalSells:
            return self.wage + (float(self.comissionPercent) * totalSells)

        return self.wage

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getComissionedAttributes(self):
        return tuple(
            [self.name, self.address, self.jType, self.payMethod, self.isInSyndicate,
             self.syndicateCharge, self.serviceCharge, self.nextPayment, self.wage, None, None, self.sellCount]
        )

    # Method that constructs our class from the result of SELECT query in database
    def constructCommsFSelect(self, SelectResult):
        self.id = None
        self.name = SelectResult.name
        self.address = SelectResult.address
        self.jType = SelectResult.jType
        self.payType = SelectResult.payType
        self.payMethod = SelectResult.payMethod
        self.isInSyndicate = SelectResult.isInSyndicate
        self.syndicateCharge = SelectResult.syndicateCharge
        self.serviceCharge = SelectResult.serviceCharge
        self.nextPayment = SelectResult.nextPayment
        self.wage = int(SelectResult.wage)
        self.sellCount = SelectResult.sellCount
        self.saleId = None
        self.saleDate = None
        self.salePrice = None
        self.buyerName = None
        self.comissionPercent = SelectResult.comissionPercent