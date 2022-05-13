
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import os

def createFolder(directory): 
    try: 
        if not os.path.exists(directory): 
            os.makedirs(directory) 
    except OSError: 
        print ('Error: Creating directory. ' + directory)

def wc2(brand, name, count):

    createFolder('./' + "향수")

    max_cnt = count
    keyword = brand + '_' + name
    keyword2 = brand + ' ' + name
    createFolder('./'+ "향수/" + keyword)

    url = f'https://www.google.co.kr/search?q={keyword2}' #구글 검색

    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click() # 이미지 배너 클릭

    elem = browser.find_element_by_tag_name("body")

    for i in range(60): 
        elem.send_keys(Keys.PAGE_DOWN) # 웹 페이지 다운
        
    try: 
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div[1]/div[4]/div[2]/input').click() 
        for i in range(60): 
            elem.send_keys(Keys.PAGE_DOWN) 
        
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

    browser.quit()



    
