from tkinter import *
from tkinter import messagebox

def clickButton():
    messagebox.showinfo('버튼클릭', '버튼을 클릭했습니다.')


window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("400x400")

button1 = Button(window, text = "요기 눌러요", fg="red", bg="yellow", command =clickButton)
button1.pack(expand = 1)  # expand 속성 버튼 1개만 올림

window. mainloop()    # 선언 필수
