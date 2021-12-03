import pymysql
from tkinter import *
from tkinter import messagebox


# 데이터베이스연동함수


def insertDate():
    conn = None
    cur = None

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
    cur= conn.cursor()

    conn.commit()
    conn.close()


def selectDate():
    conn = None
    cur = None

    lUserID, lName, lBirthYear, lAddr = [], [], [], []

    conn = pymysql.connect(host="127.0.0.1", user="root", password="1234", db="sqlDB", charset="utf8")

    cur = conn.cursor()

    lUserID.append("회원ID")
    lUserID.append("--------")

    lName.append("회원명")
    lName.append("----------")

    lBirthYear.append("회원출생연도")
    lBirthYear.append("----------")

    lAddr.append("회원주소")
    lAddr.append("-----------")
#select

    sql = "SELECT userID, name, birthYear, addr from userTBL"
    cur.execute(sql)
    while(True):
        row = cur.fetchone()

        if row == None:
            break
        lUserID.append(row[0])
        lName.append(row[1])
        lBirthYear.append(row[2])
        lAddr.append(row[3])

    # GUI ListBox에 insert
    # listUserID, listName, listBirthYear, listAddr
    # 1) 리스트 박스 초기화(기존 데이터 삭제
    listUserID.delete(0, listUserID.size() - 1)  # listUserID는 gui
    listName.delete(0, listName.size() - 1)
    listBirthYear.delete(0, listBirthYear.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)

    # 2) select 해온 데이터 insert
    for item1, item2, item3, item4 in zip(lUserID, lName, lBirthYear, lAddr):
        listUserID.insert(END, item1)
        listName.insert(END, item2)
        listBirthYear.insert(END, item3)
        listAddr.insert(END, item4)

    conn.close()
# 화면구성

window = Tk()
window.geometry("800x300")
window.title("MariaDB 연동 GUI")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side= BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text = "회원ID")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text = "회원명")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text = "회원 출생연도")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text = "회원주소")
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)


#버튼

btninsert = Button(editFrame, text = "입력", command= insertDate)
btninsert.pack(side=LEFT, padx=10, pady=10)

btnselect =  Button(editFrame, text = "조회", command= selectDate)
btnselect.pack(side=LEFT, padx=10, pady=10)

listUserID = Listbox(listFrame)
listUserID.pack(side=LEFT,fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT,fill=BOTH, expand=1)

listBirthYear = Listbox(listFrame)
listBirthYear.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT,fill=BOTH, expand=1)

window.mainloop()
