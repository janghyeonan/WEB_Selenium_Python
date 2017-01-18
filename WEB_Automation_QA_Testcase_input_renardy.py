#나의 테스트 케이스 사이트 TC생성
from selenium import webdriver
import time
import random

driver = webdriver.Chrome("D:\selenium\chromedriver.exe")

driver.set_page_load_timeout(30)

#접속한다.
driver.get("http://www.renardy.co.kr")

driver.implicitly_wait(30)
#time.sleep(10)

#암호를 입력한다.
driver.find_element_by_id("txt_pw").send_keys("암호암호")
#로그인한다.
driver.find_element_by_id("btn_login").click()

for i in range(50):
    
#test 카테고리 클릭
    driver.find_element_by_xpath("//*[@id='TreeView1n0']").click()
#새 페이지 추가 클릭
    driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_ImageButton2']").click()
#제목 입력
    driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_txt_name']").send_keys("test %d" % random.randrange(1, 10000))
#내용 입력
    driver.execute_script("document.getElementsByTagName('iframe')[0].contentWindow.document.getElementsByTagName('body')[0].getElementsByTagName('div')[58].getElementsByTagName('iframe')[0].contentWindow.document.getElementsByTagName('body')[0].append('this is test auto selenium!')")
#생성버튼 클릭
    driver.find_element_by_xpath("//*[@id='ContentPlaceHolder1_btn_save']").click()

#종료
driver.quit()
