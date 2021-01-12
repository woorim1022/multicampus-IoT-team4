import sqlite3;
from datetime import datetime

con = None;
cursor = None;

def connectDB(dbName):
    "Connect SQLite..."
    global con, cursor;
    con = sqlite3.connect(dbName);
    cursor = con.cursor();
    print('SQLite connected...');

def makeTable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
    id CHAR(16) primary key, 
    userid CHAR(16),
    itemid CHAR(16),
    price NUMBER(20),
    qt NUMBER(10),
    orderdate CHAR(16)
)""");
    print('Table Created..')

def insertOrder(order):
    "Insert User Data"
    insetSQL = """Insert into orders values ('%s','%s','%s','%d','%d','%s')""" % \
               (order[0],order[1],order[2],int(order[3]),int(order[4]),order[5]);
    cursor.execute(insetSQL);
    con.commit();



def selectOneOrder(id):
    "Select One order"
    oneOrder = [];
    selectOneSQL = """select * from orders where id='%s'""" % (id);
    cursor.execute(selectOneSQL);
    orderData = cursor.fetchone();
    oneOrder.append(orderData[0]);
    oneOrder.append(orderData[1]);
    oneOrder.append(orderData[2]);
    oneOrder.append(orderData[3]);
    oneOrder.append(orderData[4]);
    oneOrder.append(orderData[5]);
    return oneOrder;



def deleteOrder(id):
    "Delete One order"
    deleteSQL = """delete from orders where id='%s'""" % (id);
    cursor.execute(deleteSQL);
    con.commit();



def updateOrder(order):
    "Update One order"
    updateSQL = """update orders set pwd='%s',name='%s',phone='%s',addr='%s',age=%d where id='%s'""" \
                % (order[1],order[2],order[3],int(order[4]),int(order[5]),order[0]);
    cursor.execute(updateSQL);
    con.commit();



def selectOrder():
    "Select order Data"
    global con, cursor;
    cursor.execute('select * from orders');
    allorders = cursor.fetchall();
    return allorders;



def closeDB():
    "Close SQLite"
    if cursor != None:
        cursor.close();
    if con != None:
        con.close();