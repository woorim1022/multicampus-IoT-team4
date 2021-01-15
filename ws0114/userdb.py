from sqlitedb import *;
from value import *;


# 순수하게 User 관련 데이터만 조작하는 클래스
class UserDb(SqliteDb):
    def __init__(self, dbName):
        super().__init__(dbName);

    def insert(self, u):
        cc = self.getConnect();
        cc['cursor'].execute(Sql.insertUser % u.sqlmap());
        cc['con'].commit();
        self.close(cc);

    def select(self):
        cc = self.getConnect();
        cc['cursor'].execute(Sql.selectAllUser);
        result = cc['cursor'].fetchall();
        userall = [];
        for u in result:
            # u 는 튜플 형태 ( , , ,20)
            tu = User(u[0],u[1],u[2],u[3]);
            userall.append(tu);
        self.close(cc)
        return userall;

    def selectone(self, id):
        cc = self.getConnect();
        cc['cursor'].execute(Sql.selectUser % id);
        uu = cc['cursor'].fetchone();
        userone = User(uu[0], uu[1], uu[2], uu[3]);
        self.close(cc);
        return userone;

    def update(self, u):
        cc = self.getConnect();
        cc['cursor'].execute(Sql.updateUser % (u.pwd, u.name, u.age, u.id));
        cc['con'].commit();
        self.close(cc);

    @classmethod
    def delete(self, id):
        cc = self.getConnect();
        cc['cursor'].execute(Sql.deleteUser % id);
        cc['con'].commit();
        self.close(cc);


