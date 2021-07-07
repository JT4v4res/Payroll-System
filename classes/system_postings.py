import classes.employee, uuid

class PointCard(classes.employee.Hourly):
    pass

    def getPointCard(self):
        self.getCardId()

    def getCardId(self):
        if self.pointCardId == None:
            self.pointCardId = str(uuid.uuid4())
        return

    def postPointCard(self, arrival, departure):
        self.workedHours += (departure - arrival)
        return tuple(self.workedHours,self.name)

class SalePost(classes.employee.Comissioned):
    pass

    def getSale(self):
        self.getSaleId()

    def getSaleId(self):
        self.saleId = str(uuid.uuid4())

    def postNewSale(self):
        return tuple(
            [self.name, self.address, self.sell_date, self.sell_value, self.saleId]
        )

class PostNewCharge(classes.employee.Salaried):
    pass