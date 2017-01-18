#-*- coding:utf-8 -*-
from selenium import webdriver
import time as tt
import random
from datetime import date
from datetime import time
from datetime import datetime
import datetime
import glob, os
import threading
import os

#날짜로된 파일을 폴더에서 찾고, 특정 웹 페이지에 파일업로드 후 종료하기



#파일 리스트 전역변수
filelist = []

        
#날짜로 검색할려고 준비했던 것들
print("#날짜로 검색준비")
today = datetime.date.today()
kk = today.year
mm = today.month
nn = today.day -1
kk = str(kk).replace("201", "1")
if len(str(nn)) < 2 :
    nn = "0" + str(nn)
result = str(kk) + str(mm) + str(nn)

#파일명을 얻기
print("#파일명을 얻기")
target_dir = r'C:/Users/Downloads/'
for file in glob.glob(target_dir + "%s*.xlsx" %result):
    filelist.append(file)

print("잘나옴 "+filelist[0])

#크롬 열고 실행하기
print("#다시 브라우저 열고 실행하기")
driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://localhost/file.aspx")
driver.maximize_window()
driver.implicitly_wait(30)

#파일 업로드 창 띄우기
print("#파일 업로드 창 띄우기")
tt.sleep(5)
driver.find_element_by_id("FileUpload1").send_keys(filelist[0])
tt.sleep(5)
driver.find_element_by_css_selector('#Button1').click()

#10초 카운트 다운
print("10초 후 종료")
tt.sleep(10)

#종료
print("#종료")
driver.quit()
