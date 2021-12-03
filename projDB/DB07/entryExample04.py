from tkinter import *


window = Tk()
window.title("입력관련 연습")
window.geometry("200x200")


# 프레임:영역 나누기
# 엔트리 : 입력상자(사용자에게 입력받는 <input type=text))
# 리스트박스 : 목록 (결과 화면 여려개의 row로 표현)
# 프레임으로 upframe downframe 으로 영역을 나눠서 사용

upFrame = Frame(window)
upFrame.pack()

midFrame = Frame(window)
midFrame.pack()

downFrame = Frame(window)
downFrame.pack()


editBox=Entry(upFrame, width = 10)
editBox.pack(padx=20, pady=20)

button = Button(midFrame, text = "중간")
button.pack(padx=20, pady=20)

listBox = Listbox(downFrame)
listBox.pack()

listBox.insert(END,"하나")
listBox.insert(END,"둘")
listBox.insert(END,"셋")


window. mainloop()    # 선언 필수
