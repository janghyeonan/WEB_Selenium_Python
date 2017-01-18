#coding: utf-8

#레진코믹스 사이트 스크롤 진행
from selenium import webdriver
import time

#셋업
driver = webdriver.Chrome("C:\selenium_browser\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://www.lezhin.com/")
driver.implicitly_wait(30)
print("창열림")
time.sleep(1)

print("스크롤 시작1")
time.sleep(2)

#좌표 설정
a = 0
b = 100

#스크롤 내용 for문 설정
for x in range(1, 25):
    driver.execute_script("window.scrollTo(%d, %d);" %(a,b))
    a = b
    b = b + 500
    time.sleep(0.1)

#종
driver.quit()
