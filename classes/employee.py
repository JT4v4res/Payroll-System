jTypes = {"hourly": "hourly wage", "salaried": "monthly salary", "commissioned": "commission"}


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

    def getEmployeeName(self):
        return self.name

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getHourlyAttributes(self):
        return tuple(
            [self.name, self.address, self.jType, self.payMethod, self.isInSyndicate, self.syndicateCharge,
             self.serviceCharge, str(self.wage), self.pointCardId, self.workedHours, None]
        )

    def constructHourlyFSelect(self, SelectResult):
        self.id = SelectResult[0].index('id')
        self.name = SelectResult[0].index('employee_name')
        self.address = SelectResult[0].index('employee_addr')
        self.jType = SelectResult[0].index('jType')
        self.payMethod = SelectResult[0].index('PayMethod')
        self.isInSyndicate = SelectResult[0].index('isInSyndicate')
        self.syndicateCharge = SelectResult[0].index('syndicateCharge')
        self.serviceCharge = SelectResult[0].index('serviceCharge')
        self.wage = int(SelectResult[0].index('wage'))
        self.pointCardId = SelectResult[0].index('cardId')
        self.workedHours = SelectResult[0].index('workedHours')


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
        self.name = name
        self.address = address
        self.jType = job_Type
        self.payMethod = jTypes[job_Type]
        self.isInSyndicate = syndicate
        self.syndicateCharge = None
        self.serviceCharge = None
        self.wage = None
        self.sell_date = None
        self.sell_value = None
        self.sale_id = None
        self.sellCount = None

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getComissionedAttributes(self):
        return tuple(
            [self.name, self.address, self.jType, self.payMethod, self.isInSyndicate,
             self.syndicateCharge, self.serviceCharge, self.wage, None, None, self.sellCount]
        )


# This class provides our mapping and planning for implementing and manipulating
# data and other functionality relating to our payroll employees.
class Employee:
    def __init__(self, name=None, address=None, job_Type=None, syndicate=False):
        self.id = None

    # Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getEmployeeAttributes(self):
        return tuple([self.name, self.address, self.jType, self.Payment, self.isInSyndicate])

    # This method performs the reconstruction of the attributes of a given
    # employee from the data stored and required through a query in our database
    def constructFromSelect(self, SelectResult):
        self.id = SelectResult.id
        self.name = SelectResult.employee_name
        self.address = SelectResult.employee_addr
        self.jType = SelectResult.jType
        self.Payment = SelectResult.PayMethod
        self.isInSyndicate = SelectResult.isInSyndicate
        self.pointCardId = SelectResult.cardId
        self.SellResult = SelectResult.SellRes
        self.serviceCharge = SelectResult.serv_charge