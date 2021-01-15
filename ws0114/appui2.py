import wx
from userdb import *

########################################
"""
1. 화면에서 데이터를 입력하면 db에 인서트되고 리스트 화면에 출력

2. 리스트 화면에는 id와 name만 출력되고 항목을 클릭했을때
아이디 패스워드 이름 모두 출력 되게 한다.

db 연동
입력 시 db에 저장
입력값 db에서 가져와서 출력
"""




data = []
app = wx.App()
# UI Component ................................

frame = wx.Frame(None,title='Shop Management')
panel1 = wx.Panel(frame)
panel2 = wx.Panel(frame)
panel1.SetBackgroundColour(colour='blue')
panel2.SetBackgroundColour(colour='green')

textId = wx.TextCtrl(panel1)
textPwd = wx.TextCtrl(panel1)
textName = wx.TextCtrl(panel1)
textAge = wx.TextCtrl(panel1)
bt = wx.Button(panel1, label='ADD')

userList = wx.ListBox(panel2,choices=data)
userList.SetBackgroundColour(colour='white')
userList.SetSize(wx.Size(180,200))

#List Event ....................................
def itemselect(event):
    dataCnt = userList.GetSelection()
    wx.MessageBox(data[dataCnt],'User Infomation', wx.OK)

userList.Bind(wx.EVT_LISTBOX,itemselect)


# Button Event .................................
def onClick(event):
    id = textId.GetValue()
    pwd = textPwd.GetValue()
    name = textName.GetValue()
    age = textAge.GetValue()

    #객체생성
    udb = UserDb('shopdb.db');

    # insert 동작
    user = User(id, pwd, name, int(age));
    udb.insert(user);

    # select 동작
    userlist = udb.select();
    for u in userlist:
        data.append(u.id + ' ' + u.pwd + ' ' + u.name + ' ' + str(u.age))
        userList.Append(u.id + ' ' + u.name)

    wx.MessageBox(id, 'Alert', wx.OK)

    textId.SetValue('')
    textPwd.SetValue('')
    textName.SetValue('')
    textAge.SetValue('');


bt.Bind(wx.EVT_BUTTON, onClick) #이벤트 발생시 온클릭 시행

box1 = wx.BoxSizer(wx.VERTICAL)
box1.Add(textId)
box1.Add(textPwd)
box1.Add(textName)
box1.Add(textAge)
box1.Add(bt)
panel1.SetSizer(box1)

# Grid ..................................
grid = wx.GridSizer(1,2,10,10) #1행2열 양쪽 여백넓이
grid.Add(panel1,0,wx.EXPAND)
grid.Add(panel2,1,wx.EXPAND)

frame.SetSizer(grid)
frame.Show(True)
app.MainLoop()