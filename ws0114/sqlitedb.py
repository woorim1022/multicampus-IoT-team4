import sqlite3;
from value import *;

class Sql:
    makeusertb = """create table if not exists usertb(
	                id char(10) primary key,
	                pwd char(10),
	                name char(10),
	                age number(3)
    )""";
    makeitemtb = """create table if not exists itemtb(
    	                id char(10) primary key,
    	                name char(10),
    	                price number(10)
        )""";
    insertUser = """insert into usertb values('%s','%s','%s',%s)
    """;
    deleteUser = """delete from usertb where id = '%s'
    """;
    updateUser = """update usertb set pwd='%s', name='%s', age=%d where id='%s'
    """;
    selectUser = """select * from usertb where id='%s'
    """;
    selectAllUser ="""select * from usertb
    """;

    insertItem = """insert into itemtb values('%s','%s', %d)
       """;
    deleteItem = """delete from itemtb where id = '%s'
       """;
    updateItem = """update itemtb set name='%s', price='%d' where id='%s'
       """;
    selectItem = """select * from itemtb where id='%s'
       """;
    selectAllItem  = """select * from itemtb
       """;


class SqliteDb:
    #self.변수명 -> 앞에 self. 을 붙이면 클래스의 속성값이 된다.
    #클래스에 의해 만들어지는 객체의 데이터
    #this. 와 같은 역할
    def __init__(self, dbName):
        self.__dbName = dbName;

    def getConnect(self):
        con = sqlite3.connect(self.__dbName);
        cursor = con.cursor();
        print(self.__dbName+'connected...');
        return {'con':con, 'cursor':cursor};

    def close(self, cc):
        if cc['cursor'] != None:
            cc['cursor'].close();
        if cc['con'] != None:
            cc['con'].close();

    def makeTable(self):
        "Make usertb Table"
        cc = self.getConnect();
        cc['cursor'].execute(Sql.makeusertb);
        cc['cursor'].execute(Sql.makeitemtb);
        cc['con'].commit();
        self.close(cc);







