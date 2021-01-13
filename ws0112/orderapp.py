from orderutil_class import *
from ordervalue import *


print('Start ....')
orderDb = OrderDb('order.db')

orderDb.makeTable()
while True:
    orderDb = OrderDb('order.db')
    orderDb.makeTable()
    # try:
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
                     ' userid, itemid, price, qt\n'
                     '(띄어쓰기기준)')
        serialNum = orderDb.serialCnt()
        user = user.split(' ')
        order2 = Order(serialNum,serialNum[:8],user[0],user[1],user[2],user[3])
        orderDb.insertOrder(order2)

    #주문정보전체조회
    if menu =='a':
        allusers = orderDb.selectOrder()
        for i in allusers:
            print(i)

    #주문번호조회
    if menu == 's':
        pid = input('조회하실 주문번호를 입력해주세요')
        oneOrder = orderDb.selectOneOrder(pid)
        print(oneOrder)

    if menu == 'u':
        user = input('수정하실 주문번호와 정보를 입력해주세요\n'
                     'id, itemid, price, qt\n'
                     '(띄어쓰기기준)')
        user = user.split(' ')
        order2 = Order(user[0],"","",user[1], user[2], user[3])
        orderDb.updateOrder(order2)

    # 주문삭제
    if menu == 'd':
        pid = input('삭제하실 주문번호를 입력하세요')
        orderDb.deleteOrder(pid)
    #
    # except:
    #     print("에러가 발생했습니다...")


print('End ....')