#-*- coding: utf-8 -*-

#네이버 블로그 글작성
from selenium import webdriver
import time as tt
import random
from datetime import date
from datetime import time
from datetime import datetime

driver = webdriver.Chrome("D:\selenium\chromedriver.exe")

driver.set_page_load_timeout(30)
driver.maximize_window()

#접속한다.
driver.get("http://www.naver.com")
driver.implicitly_wait(30)


#로그인
driver.find_element_by_id("id").send_keys("아이디")
driver.find_element_by_id("pw").send_keys("비밀번호")
driver.find_element_by_xpath("//*[@id='frmNIDLogin']/fieldset/span/input").click()
tt.sleep(1)

#블로그로 입장
driver.find_element_by_xpath("//*[@id='svc.blog']").click()

#블로그로 입장2
driver.find_element_by_xpath("//*[@id='container']/div[3]/ul[2]/li[1]/a").click()


#글쓰기 클릭
driver.get("http://blog.naver.com/ajh910/postwrite?categoryNo=29")
driver.implicitly_wait(30)

#제목 입력
driver.find_element_by_xpath("//*[@id='subject']").clear()
driver.find_element_by_xpath("//*[@id='subject']").send_keys("안녕하세요.")
tt.sleep(5)


#내용입력.
driver.switch_to_frame(0)
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_css_selector("body").send_keys("hello")
driver.switch_to_frame(0)
ab = driver.find_element_by_css_selector('div.se_editView div.se_textView>div>div')
ab.send_keys("아아")

#작성완료 버튼 클릭
driver.find_element_by_xpath("//*[@id='btn_submit']/img").click()


#종료
driver.quit()
