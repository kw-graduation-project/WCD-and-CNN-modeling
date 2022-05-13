import tkinter.ttk as ttk
from tkinter import *
from WCC import *
from selenium import webdriver
import sys, os
import time
import tkinter.messagebox as msgbox

if  getattr(sys, 'frozen', False): 
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")


root = Tk()

root.wm_attributes("-topmost", 1)

root.title("WCD GUI") # 타이틀
root.geometry("640x480+300+100" ) # 가로 x 세로 크기 + x좌표 + y 좌표
root.resizable(False, False)

label1 = Label(root, text="사진 개수 선택:")
label1.place(x=260, y=70)

photo_count = IntVar()
btn_20 = Radiobutton(root, text = "20장", value = 20, variable=photo_count)
btn_20.select()
btn_40 = Radiobutton(root, text = "40장", value = 40, variable=photo_count)
btn_60 = Radiobutton(root, text = "60장", value = 60, variable=photo_count)

btn_20.place(x=280, y=100)
btn_40.place(x=280, y=120)
btn_60.place(x=280, y=140)

e1 = Entry(root, width = 15)
e1.place(x=200, y=200)
e1.insert(0, "브랜드")

e2 = Entry(root, width = 15)
e2.place(x=320, y=200)
e2.insert(0, "제품명")

def e1_click(event):
    if e1.get() == "브랜드":
        e1.delete(0, END)

e1.bind("<ButtonRelease-1>", e1_click)

def e2_click(event):
    if e2.get() == "제품명":
        e2.delete(0, END)

e2.bind("<ButtonRelease-1>", e2_click)


def btncmd():
    wc2(e1.get(), e2.get(), photo_count.get())
    msgbox.showinfo("알림", "다운로드 완료")

    


btn1 = Button(root, text ="다운로드", command=btncmd)
btn1.place(x=280, y=240)

p_var1 = DoubleVar()
progressbar1 = ttk.Progressbar(root, maximum=100, length = 400, variable=p_var1)
progressbar1.place(x=120, y=400)


root.mainloop()