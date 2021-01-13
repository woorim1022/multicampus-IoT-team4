import sqlite3;
import datetime
from ordervalue import *

class Sql:
    # 클래스변수
    # sql문은 이 클래스에서만 관리
    makeTable = """
        CREATE TABLE IF NOT EXISTS orders(
            id CHAR(16) primary key,
            date CHAR(16),
            userid CHAR(16),
            itemid CHAR(16),
            price NUMBER(10),
            qt NUMBER(10)
            )"""
    insetSQL = """Insert into orders values ('%s','%s','%s','%s','%s','%s')"""
    selectOrder = """select * from orders where id='%s'"""
    selectAll = """select * from orders"""
    deleteOrder = """delete from orders where id='%s'"""
    updateOrder = """update orders set itemid='%s',price='%s',qt='%s' where id='%s'"""


class OrderDb:

    def __init__(self,dbName):
        self.__dbName = dbName
    
    def connectDB(self):
        "Connect SQLite..."
        con = sqlite3.connect(self.__dbName)
        cursor = con.cursor()
        return {'con':con, 'cursor':cursor}

    def closeDB(self,cc):
        "Close SQLite"
        if cc['cursor'] != None:
            cc['cursor'].close()
        if cc['con'] != None:
            cc['con'].close()

    def makeTable(self):
        "Make order Table"
        cc = self.connectDB()
        cc['cursor'].execute(Sql.makeTable)
        cc['con'].commit()
        self.closeDB(cc)

    def insertOrder(self, order):
        "Insert order Data"
        cc = self.connectDB()
        cc['cursor'].execute(Sql.insetSQL % (order.sqlmap()));
        cc['con'].commit();
        self.closeDB(cc)

    def selectOrder(self):
        "Select order Data"
        cc = self.connectDB()
        cc['cursor'].execute(Sql.selectAll)
        allorders = cc['cursor'].fetchall()
        userall = []
        for u in allorders:
            t = Order(u[0],u[1],u[2],u[3],u[4],u[5])
            userall.append(t)
        self.closeDB(cc)
        return userall

    def selectOneOrder(self, id):
        "Select One order"
        cc = self.connectDB()
        cc['cursor'].execute(Sql.selectOrder % (id))
        data = cc['cursor'].fetchone();
        orderData = Order(data[0],data[1],data[2],data[3],data[4],data[5])
        self.closeDB(cc)
        return orderData
    #delete문 함수
    def deleteOrder(self, id):
        "Delete One order"
        cc = self.connectDB()
        cc['cursor'].execute(Sql.deleteOrder % (id));
        cc['con'].commit();
        self.closeDB(cc)

    #update문 함수
    def updateOrder(self, order):
        "Update One order"
        cc = self.connectDB()
        cc['cursor'].execute(Sql.updateOrder % (order.itemid, order.price, order.qt, order.id));
        cc['con'].commit();
        self.closeDB(cc)
    
    #주문번호 구하는 함수
    def serialCnt(self):
        cc = self.connectDB()
        cc['cursor'].execute(Sql.selectAll);
        allorders = cc['cursor'].fetchall();
        
        list = []
        if len(allorders) == 0:
            serial = self.dateNow() + str(1)
        else:
            for i in range(len(allorders)):
                list.append(int(allorders[i][0][8:]));
            serial = self.dateNow() + str(max(list) + 1);
        self.closeDB(cc)
        return serial;
    
    #date날짜 구하는 함수
    @classmethod
    def dateNow(cls):
        t = str(datetime.datetime.now());
        t = t[:10];
        t = t.split(sep='-');
        return t[0] + t[1] + t[2];
