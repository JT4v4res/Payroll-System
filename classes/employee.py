import uuid

types = {"hourly":"hourly wage", "salaried":"monthly salary", "commissioned":"commission"}

#This class provides our mapping and planning for implementing and manipulating
#data and other functionality relating to our payroll employees.
class Employee():
    def __init__(self, name=None, address=None, job_Type=None, syndicate=False):
        self.id = None
        self.name = name
        self.address = address
        self.jType = job_Type
        self.Payment = types[self.jType]
        self.isInSyndicate = syndicate
        self.pointCardId = self.isHourlyEmployee(job_Type)
        self.SellResult = None
        self.serviceCharge = None

    #Method that returns our character's attributes as a tuple so we can access
    # them without having to directly access the attributes in the class
    def getEmployeeAttributes(self):
        return tuple([self.name,self.address,self.jType,self.Payment,self.isInSyndicate])

    #This method serves to create a unique identification
    #for the points card for our employees
    def isHourlyEmployee(self, job):
        if job == self.jType:
            return str(uuid.uuid4())
        return None

    #This method performs the reconstruction of the attributes of a given
    #employee from the data stored and required through a query in our database
    def constructFromSelect(self, SelectResult):
        self.id = SelectResult.id
        self.name = SelectResult.employee_name
        self.address = SelectResult.employee_addr
        self.jType = SelectResult.jType
        self.Payment = SelectResult.PayMethod
        self.isInSyndicate = SelectResult.syndicate
        self.pointCardId = SelectResult.cardId
        self.SellResult = SelectResult.SellRes
        self.serviceCharge = SelectResult.serv_charge