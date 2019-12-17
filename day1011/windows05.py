from tkinter import *   # 윈도우 위젯을 지원하는 라이브러리
from tkinter import  messagebox  # 대화상자를 지원하는 함수

def myFunc():
    messagebox.showinfo("축구 버튼", "멋진 크로스")


window = Tk()
window.title("이미지 클릭시 메시지박스")
window.geometry("400x200")

photo = PhotoImage(file="BothNeatArcticseal-size_restricted.gif")
button = Button(window, image=photo, command=myFunc)

button.pack()
window.mainloop()