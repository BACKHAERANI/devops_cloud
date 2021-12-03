import pymysql
from tkinter import *
from tkinter import messagebox




def backFrame():
    editFrame.pack()
    pLabel.pack()
    listFrame.pack_forget()

#-----------------------------------------------------

def insertDate():
    conn = None
    cur = None

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hrent', charset='utf8')
    cur= conn.cursor()


    id,name, birth, gender, posi,score = "","","","","",""

    id = edt0.get()
    name = edt1.get()
    birth = edt2.get()
    gender= edt3.get()
    posi = edt4.get()
    score = edt5.get()

    sql = ""
    sql = "INSERT INTO raspberrypyTBL(id, name, birth, gender, posi, score) VALUES ('"+id+"',' '" + name + "'," + birth + ",'" + gender + "','" + posi + "',"+score+")"



    try:
        cur.execute(sql)
    except:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생했습니다.")
    else:
        messagebox.showinfo("성공", "연습생정보가 등록 되었습니다.")
        conn.commit()
        selectDate()

    #gul 입력한 데이터 삭제
    edt0.delete(0,"end")
    edt1.delete(0,"end")
    edt2.delete(0,"end")
    edt3.delete(0,"end")
    edt4.delete(0,"end")
    edt5.delete(0,"end")


    conn.close()

#-------------------------------------------------------------------------------------

def selectDate():
    conn = None
    cur = None

    name = edt1.get()
    editFrame.pack_forget()
    pLabel.pack_forget()
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)



    lid,lname, lbirth, lgender, lposi, lscore = [], [], [], [], [],[]


    conn = pymysql.connect(host="127.0.0.1", user="root", password="1234", db="hrent", charset="utf8")

    cur = conn.cursor()

    lid.append("아이디")
    lid.append("---------")

    lname.append("이름")
    lname.append("--------")

    lbirth.append("생일")
    lbirth.append("----------")

    lgender.append("성별")
    lgender.append("----------")

    lposi.append("예상포지션")
    lposi.append("-----------")

    lscore.append("월말평가점수")
    lscore.append("-----------")

    sql = "SELECT id, name, birth, gender, posi,score from raspberrypytbl ORDER BY id DESC"
    cur.execute(sql)
    while (True):
        row = cur.fetchone()

        if row == None:
            break
        lid.append(row[0])
        lname.append(row[1])
        lbirth.append(row[2])
        lgender.append(row[3])
        lposi.append(row[4])
        lscore.append(row[5])

    # 1) 리스트 박스 초기화(기존 데이터 삭제
    listID.delete(0, listname.size() - 1)
    listname.delete(0, listname.size() - 1)  # listUserID는 gui
    listbirth.delete(0, listbirth.size() - 1)
    listgender.delete(0, listgender.size() - 1)
    listposi.delete(0, listposi.size() - 1)
    listscore.delete(0, listscore.size() - 1)

    # 2) select 해온 데이터 insert
    for item0, item1, item2, item3, item4, item5 in zip(lid, lname, lbirth, lgender, lposi, lscore):
        listID.insert(END, item0)
        listname.insert(END, item1)
        listbirth.insert(END, item2)
        listgender.insert(END, item3)
        listposi.insert(END, item4)
        listscore.insert(END, item5)


    conn.close()


#-------------------------------------------------------------------------------------------------------

def selectData():
    conn = None
    cur = None

    name = edt1.get()
    editFrame.pack_forget()
    pLabel.pack_forget()
    listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

    lid, lname, lbirth, lgender, lposi, lscore = [], [], [], [], [], []

    conn = pymysql.connect(host="127.0.0.1", user="root", password="1234", db="hrent", charset="utf8")

    cur = conn.cursor()

    lid.append("아이디")
    lid.append("---------")

    lname.append("이름")
    lname.append("--------")

    lbirth.append("생일")
    lbirth.append("----------")

    lgender.append("성별")
    lgender.append("----------")

    lposi.append("예상포지션")
    lposi.append("-----------")

    lscore.append("월말평가점수")
    lscore.append("-----------")


    sql = "SELECT id, name, birth, gender, posi,score from raspberrypytbl where name= '"+name+"' ORDER BY score DESC"
    cur.execute(sql)
    while(True):
        row = cur.fetchone()

        if row == None:
            break
        lid.append(row[0])
        lname.append(row[1])
        lbirth.append(row[2])
        lgender.append(row[3])
        lposi.append(row[4])
        lscore.append(row[5])

    listID.delete(0, listID.size() -1)
    listname.delete(0, listname.size() - 1)
    listbirth.delete(0, listbirth.size() - 1)
    listgender.delete(0, listgender.size() - 1)
    listposi.delete(0, listposi.size() - 1)
    listscore.delete(0, listscore.size() - 1)


    for item0, item1, item2, item3, item4, item5 in zip(lid,lname, lbirth, lgender, lposi, lscore):
        listID.insert(END,item0)
        listname.insert(END, item1)
        listbirth.insert(END, item2)
        listgender.insert(END, item3)
        listposi.insert(END, item4)
        listscore.insert(END, item5)

    edt1.delete(0, "end")

    conn.close()

#-----------------------------------------------------------------------------------------------------------------

def deleteData():
    conn = None
    cur = None

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hrent', charset='utf8')

    cur = conn.cursor()

    id = listID.get(listID.curselection())


    sql = "DELETE FROM raspberrypytbl WHERE id = '"+id+"'"

    answer = messagebox.askokcancel("경고", "연습생 정보를 삭제하시겠습니까?")

    if answer :
        try:
            cur.execute(sql)
        except:
            messagebox.showerror("삭제오류", "데이터 삭제 오류가 발생 했습니다.")
        else:
            conn.commit()
            selectDate()

    conn.close()

# 화면구성----------------------------------------------------------------------------------------------------

window = Tk()
window.geometry("1400x480")
window.title("hrent raspberrypy project")

photo1 = PhotoImage(file="C:\Dev\hr.png")
pLabel = Label(window, image=photo1)
pLabel.pack(side= BOTTOM, padx=10, pady=10)

editFrame = Frame(window, bg = 'gold')
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side= BOTTOM, fill=BOTH, expand=1)
listFrame.pack_forget()

label0 = Label(editFrame, text = "아이디:")
label0.pack(side=LEFT, padx=10, pady=10)

edt0 = Entry(editFrame, width=10)
edt0.pack(side=LEFT, padx=10, pady=10)

label1 = Label(editFrame, text = "연습생 이름:")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text = "생년월일:")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text = "성별:")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text = "예상포지션:")
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

label5 = Label(editFrame, text = "월말평가점수:")
label5.pack(side=LEFT, padx=10, pady=10)

edt5 = Entry(editFrame, width=10)
edt5.pack(side=LEFT, padx=10, pady=10)


#버튼

btninsert = Button(editFrame, text = "입력", command= insertDate)
btninsert.pack(side=LEFT, padx=10, pady=10)

btnselect =  Button(editFrame, text = "연습생전체", command= selectDate)
btnselect.pack(side=LEFT, padx=10, pady=10)

btnselect1 =  Button(editFrame, text = "연습생조회", command= selectData)
btnselect1.pack(side=LEFT, padx=10, pady=10)

btnre =  Button(listFrame, text = "돌아가기", command= backFrame)
btnre.pack(side=BOTTOM, padx=10, pady=10)

btnre1 = Button(listFrame, text = "삭제", command= deleteData)
btnre1.pack(side=RIGHT, padx=10, pady=10)


listID = Listbox(listFrame)
listID.pack(side=LEFT,fill=BOTH, expand=1)

listname = Listbox(listFrame)
listname.pack(side=LEFT,fill=BOTH, expand=1)

listbirth = Listbox(listFrame)
listbirth.pack(side=LEFT,fill=BOTH, expand=1)

listgender = Listbox(listFrame)
listgender.pack(side=LEFT, fill=BOTH, expand=1)

listposi = Listbox(listFrame)
listposi.pack(side=LEFT,fill=BOTH, expand=1)

listscore = Listbox(listFrame)
listscore.pack(side=LEFT,fill=BOTH, expand=1)



def func_open():
    messagebox.showinfo("데뷔조","아직미정")

def func_exit():
    window.quit()
    window.destroy()



mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="메뉴", menu=fileMenu)
fileMenu.add_command(label="데뷔조", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command = func_exit)




window.mainloop()



