from tkinter import *   # 윈도우 위젯을 지원하는 라이브러리

window = Tk()
window.geometry("400x200")

button = Button(window, text="파이썬종료", fg="red", command=quit)

button.pack()

window.mainloop()