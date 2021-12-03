from tkinter import *
from tkinter import messagebox


def clickButton():
    messagebox.showinfo('버튼클릭', '버튼을 클릭했습니다.')

window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")

button1 = Button(window, text = "버튼",  fg="red", bg="yellow", command =clickButton)
button2 = Button(window, text = "버튼1", fg="red", bg="yellow", command =clickButton)
button3 = Button(window, text = "버튼2", fg="red", bg="yellow", command =clickButton)

button1.pack(side=TOP, padx=10, pady=10)
button2.pack(side=TOP, padx=10, pady=10)
button3.pack(side=TOP, padx=10, pady=10)

window. mainloop()    # 선언 필수
