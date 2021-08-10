import uuid
from datetime import datetime
from classes import employee
from classes import sqlmanager
from sqlalchemy import Column, String, Date, Integer


class Sales(sqlmanager.Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True, nullable=False)
    saleId = Column(String(80))
    sellerName = Column(String(55))
    buyerName = Column(String(55))
    saleDate = Column(Date)
    salePrice = Column(String(10))

    def __init__(self, saleId, sellerName, buyerName, saleDate, salePrice):
        self.saleId = saleId
        self.sellerName = sellerName
        self.buyerName = buyerName
        self.saleDate = saleDate
        self.salePrice = salePrice


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
        self.saleDate = datetime.today().strftime('%Y-%m-%d')
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


class PostNewCharge(employee.Salaried):
    pass