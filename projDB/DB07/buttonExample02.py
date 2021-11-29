from tkinter import *
from tkinter import messagebox

def clickButton():
    messagebox.showinfo('버튼클릭', '버튼을 클릭했습니다.')


window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")

button1 = Button(window, text = "요기 눌러요", fg="red", bg="yellow", command =clickButton)
button1.pack(expand = 1)

window. mainloop()    # 선언 필수
