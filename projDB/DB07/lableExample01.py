from tkinter import *
window = Tk()

#문자를 표현할 수 있는 라벨 사용

window.title("라벨 연습")
window.geometry("400x100")

lable1 = Label(window, text= 'This is MariaDB를')
lable1 = Label(window, text= 'This is MariaDB를')
lable2 = Label(window, text= '열심히', font=("궁서체", 30), fg="blue")
lable3 = Label(window, text= '공부 중입니다.', bg="magenta", width = 20, height = 5, anchor=SE)   #anchor 글자위치

lable1.pack()    #실제로 위젯 적용 pack
lable2.pack()
lable3.pack()

window. mainloop()    # 선언 필수
