import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os
import tkinter.ttk as ttk
from tkinter import *
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


def createFolder(directory): 
    try: 
        if not os.path.exists(directory): 
            os.makedirs(directory) 
    except OSError: 
        print ('Error: Creating directory. ' + directory)


idx2 = 0

def wc2(brand, name, count):

    global idx2

    createFolder('./' + "향수")

    max_cnt = count
    keyword = brand + '_' + name
    keyword2 = brand + ' ' + name # 띄어쓰기 된 이름
    createFolder('./'+ "향수/" + keyword)

    url = f'https://www.google.co.kr/search?q={keyword2}' #구글 검색

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() # 이미지 배너 클릭

    elem = browser.find_element_by_tag_name("body")

    for i in range(60): 
        elem.send_keys(Keys.PAGE_DOWN) # 웹 페이지 다운
        time.sleep(0.2)
        
    try: 
        browser.find_element_by_xpath('//*[@id="islmp"]/div/div/div[2]/div[1]/div[2]/div[2]/input').click() 
        for i in range(60): 
            elem.send_keys(Keys.PAGE_DOWN) 
            time.sleep(0.1)
        
    except: 
        pass


    links=[] 
    images = browser.find_elements_by_css_selector("img.rg_i.Q4LuWd") 
    idx = 1
    for image in images: 
        if image.get_attribute('src')!=None: 
            links.append(image.get_attribute('src'))
            idx += 1
        if idx > count:
            break

    
    for k,i in enumerate(links): 
        url = i 
        urllib.request.urlretrieve(url, "./"+ "향수/" +keyword +"/" +keyword + "_" + str(k+1)+".jpg")
        p_var1.set((k+1/idx) * 100)
        progressbar1.update()
        idx2 = k+1
        

    browser.quit()


def btncmd():
    wc2(e1.get(), e2.get(), photo_count.get())
    msgbox.showinfo("알림", f"총 {idx2}장 다운로드 완료")

    


btn1 = Button(root, text ="다운로드", command=btncmd)
btn1.place(x=280, y=240)

p_var1 = DoubleVar()
progressbar1 = ttk.Progressbar(root, maximum=100, length = 400, variable=p_var1)
progressbar1.place(x=120, y=400)


root.mainloop()