import sqlite3
import orderutil

print('Start ....')
while True:
    orderutil.connectDB('order.db')
    orderutil.makeTable()
    try:
        menu = input('***주문테이블구성***\n'
                     '주문추가(i)\n'
                     '주문정보전체조회(a)\n'
                     '주문번호조회(s)\n'
                     '주문삭제(d)\n'
                     '주문수정(u)\n'
                     '나가기(q)');
        menu = menu.lower()
        if menu == 'q':
            print('Bye')
            break
        #주문추가
        if menu == 'i':
            user = input('추가할 주문정보를 입력하세요\n'
                         'id, userid, itemid, price, qt\n'
                         '(띄어쓰기기준)')
            user = user.split(' ')
            userdata = []
            for u in user:
                userdata.append(u)
            orderutil.insertOrder(userdata)
        #주문정보전체조회
        if menu =='a':
            allusers = orderutil.selectOrder()
            for u in allusers:
                print("%s,%s,%s,%s,%s,%s" % (u[0],u[1],u[2],u[3],u[4],u[5]))
        #주문번호조회
        if menu == 's':
            pid = input('조회하실 주문번호를 입력해주세요')
            oneUser = orderutil.selectOneOrder(pid)
            print(oneUser)
        #주문삭제
        if menu == 'd':
            pid = input('삭제하실 주문번호를 입력하세요')
            orderutil.deleteOrder(pid)
        if menu == 'u':
            info = input('수정하실 주문정보를 입력해주세요\n'
                         'pid, itemid, price, qt\n'
                         '(띄어쓰기기준)')
            info = info.split(' ')
            orderdata = []
            for u in info:
                orderdata.append(u)
            orderutil.updateOrder(orderdata)
    except:
        print("에러가 발생했습니다...")
    finally:
        orderutil.closeDB()


print('End ....')