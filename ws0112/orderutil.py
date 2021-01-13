import sqlite3;
import datetime
from orderutil_class import Sql;

con = None;
cursor = None;

def connectDB(dbName):
    "Connect SQLite..."
    global con, cursor;
    con = sqlite3.connect(dbName);
    cursor = con.cursor();
    print('SQLite connected...');

def makeTable():
    "Make order Table"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id CHAR(16) primary key,
        date CHAR(16),
        userid CHAR(16),
        itemid CHAR(16),
        price NUMBER(10),
        qt NUMBER(10)
        )""")
    con.commit()

#
# def dateNow2():
#     now = datetime.datetime.now()
#     print(now.strftime('%Y-%m-%d'))

def dateNow():
    t = str(datetime.datetime.now());
    t = t[:10];
    t = t.split(sep='-');
    return t[0]+t[1]+t[2];

def insertOrder(order):
    "Insert order Data"
    insetSQL = Sql.insetSQL % \
               (order[0],dateNow(),order[1],order[2],int(order[3]),int(order[4]));
    cursor.execute(insetSQL);
    con.commit();



def selectOneOrder(id):
    "Select One order"
    order = [];
    selectOneSQL = Sql.selectOrder % (id);
    cursor.execute(selectOneSQL);
    orderData = cursor.fetchone();
    order.append(orderData[0]);
    order.append(orderData[1]);
    order.append(orderData[2]);
    order.append(orderData[3]);
    order.append(orderData[4]);
    order.append(orderData[5]);
    return order;



def deleteOrder(id):
    "Delete One order"
    deleteSQL = Sql.deleteOrder % (id);
    cursor.execute(deleteSQL);
    con.commit();



def updateOrder(order):
    "Update One order"
    updateSQL = Sql.updateOrder \
                % (order[1],int(order[2]),int(order[3]),order[0]);
    cursor.execute(updateSQL);
    con.commit();



def selectOrder():
    "Select order Data"
    global con, cursor;
    cursor.execute();
    allorders = cursor.fetchall();
    return allorders;



def closeDB():
    "Close SQLite"
    if cursor != None:
        cursor.close();
    if con != None:
        con.close();