import uuid
import datetime as dt
from classes import employee
from classes import sqlmanager


class PaymentSchedule:
    def __init__(self):
        pass

    def payWeekly(self, days=0, value=None):
        DbManager = sqlmanager.SQLManager()

        date = dt.date.today()

        z = 0
        while z <= days:
            name_list = DbManager.searchInTable('hourly', 2)

            if name_list:
                lgt = len(name_list)

                c = 0
                if not value:
                    while c < lgt:
                        if name_list[c]:
                            Func = employee.Hourly()
                            Func.constructHourlyFSelect(DbManager.searchInTable(name_list[c], 0))

                            if date == Func.nextPayment and Func.payType.lower() == 'hourly wage':
                                Extra = Func.getExtraWorkHours()
                                Normal = Func.workedHours - Extra

                                if Extra == 0:
                                    Extra = 1
                                if Normal == 0:
                                    Normal = 1

                                Payment = (Normal * Func.wage) + ((Extra * Func.wage) * 1.5)\
                                          - (Func.serviceCharge + Func.syndicateCharge)

                                DbManager.updateTable(name_list[c], up_op=6, date=date)

                                print("-----------------------")
                                print("Payment Done")
                                print("Employee: ", Func.getEmployeeName())
                                print("Value: ", Payment)
                                print("Paymethod: ", Func.payMethod)
                                print("Date: ", date)
                                print("-----------------------")
                        c += 1
                else:
                    while c < lgt:
                        if name_list[c]:
                            Func = employee.Hourly()
                            Func.constructHourlyFSelect(DbManager.searchInTable(name_list[c], 0))

                            if Func.payType.lower() == 'monday':
                                if date.weekday() == 0:
                                    Extra = Func.getExtraWorkHours()
                                    Normal = Func.workedHours - Extra

                                    if Extra == 0:
                                        Extra = 1
                                    if Normal == 0:
                                        Normal = 1

                                    Payment = (Normal * Func.wage) + ((Extra * Func.wage) * 1.5) \
                                              - (Func.serviceCharge + Func.syndicateCharge)

                                    DbManager.updateTable(name_list[c], up_op=6, date=date)

                                    print("-----------------------")
                                    print("Payment Done")
                                    print("Employee: ", Func.getEmployeeName())
                                    print("Value: ", Payment)
                                    print("Paymethod: ", Func.payMethod)
                                    print("Date: ", date)
                                    print("-----------------------")
                            elif Func.payType.lower() == 'tuesday':
                                if date.weekday() == 1:
                                    Extra = Func.getExtraWorkHours()
                                    Normal = Func.workedHours - Extra

                                    if Extra == 0:
                                        Extra = 1
                                    if Normal == 0:
                                        Normal = 1

                                    Payment = (Normal * Func.wage) + ((Extra * Func.wage) * 1.5) \
                                              - (Func.serviceCharge + Func.syndicateCharge)

                                    DbManager.updateTable(name_list[c], up_op=6, date=date)

                                    print("-----------------------")
                                    print("Payment Done")
                                    print("Employee: ", Func.getEmployeeName())
                                    print("Value: ", Payment)
                                    print("Paymethod: ", Func.payMethod)
                                    print("Date: ", date)
                                    print("-----------------------")
                            elif Func.payType.lower() == 'wednessday':
                                if date.weekday() == 2:
                                    Extra = Func.getExtraWorkHours()
                                    Normal = Func.workedHours - Extra

                                    if Extra == 0:
                                        Extra = 1
                                    if Normal == 0:
                                        Normal = 1

                                    Payment = (Normal * Func.wage) + ((Extra * Func.wage) * 1.5) \
                                              - (Func.serviceCharge + Func.syndicateCharge)

                                    DbManager.updateTable(name_list[c], up_op=6, date=date)

                                    print("-----------------------")
                                    print("Payment Done")
                                    print("Employee: ", Func.getEmployeeName())
                                    print("Value: ", Payment)
                                    print("Paymethod: ", Func.payMethod)
                                    print("Date: ", date)
                                    print("-----------------------")
                            elif Func.payType.lower() == 'thursday':
                                if date.weekday() == 3:
                                    Extra = Func.getExtraWorkHours()
                                    Normal = Func.workedHours - Extra

                                    if Extra == 0:
                                        Extra = 1
                                    if Normal == 0:
                                        Normal = 1

                                    Payment = (Normal * Func.wage) + ((Extra * Func.wage) * 1.5) \
                                              - (Func.serviceCharge + Func.syndicateCharge)

                                    DbManager.updateTable(name_list[c], up_op=6, date=date)

                                    print("-----------------------")
                                    print("Payment Done")
                                    print("Employee: ", Func.getEmployeeName())
                                    print("Value: ", Payment)
                                    print("Paymethod: ", Func.payMethod)
                                    print("Date: ", date)
                                    print("-----------------------")
                            elif Func.payType.lower() == 'friday':
                                if date.weekday() == 4:
                                    Extra = Func.getExtraWorkHours()
                                    Normal = Func.workedHours - Extra

                                    if Extra == 0:
                                        Extra = 1
                                    if Normal == 0:
                                        Normal = 1

                                    Payment = (Normal * Func.wage) + ((Extra * Func.wage) * 1.5) \
                                              - (Func.serviceCharge + Func.syndicateCharge)

                                    DbManager.updateTable(name_list[c], up_op=6, date=date)

                                    print("-----------------------")
                                    print("Payment Done")
                                    print("Employee: ", Func.getEmployeeName())
                                    print("Value: ", Payment)
                                    print("Paymethod: ", Func.payMethod)
                                    print("Date: ", date)
                                    print("-----------------------")

                        c += 1
            else:
                return
            z += 1
            date += dt.timedelta(1)

    def pay2Weekly(self, days=0, value=None):
        DbManager = sqlmanager.SQLManager()

        date = dt.date.today()

        z = 0
        while z <= days:
            name_list = DbManager.searchInTable('commissioned', 2)

            if name_list:
                lgt = len(name_list)

                c = 0
                if not value:
                    while c < lgt:
                        if name_list[c]:
                            cmsd = employee.Comissioned()

                            cmsd.constructCommsFSelect(DbManager.searchInTable(name_list[c], 0))

                            if date == cmsd.nextPayment and cmsd.payType.lower() == 'commission':
                                Payment = cmsd.getPayment(cmsd.getEmployeeName()) - \
                                          (cmsd.syndicateCharge + cmsd.serviceCharge)

                                DbManager.updateTable(name_list[c], up_op=6, date=date)

                                print("-----------------------")
                                print("Payment Done")
                                print("Employee: ", cmsd.getEmployeeName())
                                print("Value: ", Payment)
                                print("Paymethod: ", cmsd.payMethod)
                                print("Date: ", date)
                                print("-----------------------")
                        c += 1
            else:
                return
            z += 1
            date += dt.timedelta(1)

    def payMonthly(self, days=0, value=None):
        DbManager = sqlmanager.SQLManager()

        date = dt.date.today()

        z = 0
        while z <= days:
            name_list = DbManager.searchInTable('salaried', 2)

            if name_list:
                lgt = len(name_list)

                c = 0
                if not value:
                    while c < lgt:
                        if name_list[c]:
                            sal = employee.Salaried()

                            sal.constructSalFSelect(DbManager.searchInTable(name_list[c], 0))

                            if date == sal.nextPayment and sal.payType.lower() == 'monthly salary':
                                Payment = sal.wage - sal.syndicateCharge + sal.serviceCharge

                                DbManager.updateTable(name_list[c], up_op=6, date=date)

                                print("-----------------------")
                                print("Payment Done")
                                print("Employee: ", sal.getEmployeeName())
                                print("Value: ", Payment)
                                print("Paymethod: ", sal.payMethod)
                                print("Date: ", date)
                                print("-----------------------")
                        c += 1
            else:
                return
            z += 1
            date += dt.timedelta(1)

    def PersoPayment(self, days=0):
        z = 0
        while z <= days:
            self.payWeekly(days, 1)
            self.pay2Weekly(days, 1)
            self.payMonthly(days, 1)
            z += 1

class PointCard(employee.Hourly):
    pass

    def getPointCard(self):
        self.getCardId()

    def getCardId(self):
        if self.pointCardId == None:
            self.pointCardId = str(uuid.uuid4())
        return

    def postPointCard(self, arrival, departure):
        self.workedHours += (departure - arrival)
        return self.workedHours


class SalePost(employee.Comissioned):
    pass

    # Method that generate a uuid for the sale transaction and get the
    # details of the sale
    def getSale(self, buyerName, value):
        self.buyerName = buyerName
        self.salePrice = value
        self.saleDate = dt.date.today().strftime('%Y-%m-%d')
        self.sellCount += 1
        self.getSaleId()

    # Method that trully generates the uuid for transaction
    def getSaleId(self):
        self.saleId = str(uuid.uuid4())

    # Method that returns the informations stored of sale
    def postNewSale(self):
        return list(
            [self.saleId, self.name, self.buyerName, self.saleDate, self.salePrice]
        )