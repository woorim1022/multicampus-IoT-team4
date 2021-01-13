import sqlite3;
import datetime

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
    insetSQL = """Insert into orders values ('%s','%s','%s','%s','%d','%d')"""
    selectOrder = """select * from orders where id='%s'""";
    selectAll = 'select * from orders';
    deleteOrder = """delete from orders where id='%s'"""
    updateOrder = """update orders set itemid='%s',price=%d,qt=%d where id='%s'"""

class OrderDb:
    con = None;
    cursor = None;
    id = ''
    serial = 1

    @classmethod
    def serialCnt(cls):
        allorders = OrderDb.selectOrder()
        list = [];
        if len(allorders) == 0:
            OrderDb.serial = OrderDb.dateNow() + str(1)
        else:
            for i in range(len(allorders)):
                list.append(int(allorders[i][0][8:]));
            OrderDb.serial = str(OrderDb.dateNow()) + str(max(list) + 1) ;

        return OrderDb.serial;

    def __init__(self):
        ""


    def connectDB(self, dbName):
        "Connect SQLite..."
        OrderDb.con = sqlite3.connect(dbName);
        OrderDb.cursor = OrderDb.con.cursor();
        print('SQLite connected...');


    def makeTable(self):
        "Make order Table"
        OrderDb.cursor.execute(Sql.makeTable)
        OrderDb.con.commit()

    @classmethod
    def dateNow(cls):
        t = str(datetime.datetime.now());
        t = t[:10];
        t = t.split(sep='-');
        return t[0] + t[1] + t[2];

    def insertOrder(self, order):
        "Insert order Data"
        serialNum = OrderDb.serialCnt()
        insetSQL = Sql.insetSQL % \
                   (serialNum, serialNum[0:8], order[0], order[1], int(order[2]), int(order[3]));
        OrderDb.cursor.execute(insetSQL);
        OrderDb.con.commit();

    def selectOneOrder(self, id):
        "Select One order"
        selectOneSQL = Sql.selectOrder % (id);
        OrderDb.cursor.execute(selectOneSQL);
        orderData = OrderDb.cursor.fetchone();
        self.__id = orderData[0];
        self.__userid = orderData[1];
        self.__itemid = orderData[2];
        self.__price = orderData[3];
        self.__qt = orderData[4];
        self.__date = orderData[5];
        return self.__id, self.__userid, self.__itemid, self.__price, self.__qt, self.__date

    def deleteOrder(self, id):
        "Delete One order"
        deleteSQL = Sql.deleteOrder % (id);
        OrderDb.cursor.execute(deleteSQL);
        OrderDb.con.commit();

    def updateOrder(self, order):
        "Update One order"
        updateSQL = Sql.updateOrder \
                    % (order[1], int(order[2]), int(order[3]), order[0]);
        OrderDb.cursor.execute(updateSQL);
        OrderDb.con.commit();

    @classmethod
    def selectOrder(self):
        "Select order Data"
        OrderDb.cursor.execute(Sql.selectAll);
        allorders = OrderDb.cursor.fetchall();
        return allorders;

    def closeDB(self):
        "Close SQLite"
        if OrderDb.cursor != None:
            OrderDb.cursor.close();
        if OrderDb.con != None:
            OrderDb.con.close();
