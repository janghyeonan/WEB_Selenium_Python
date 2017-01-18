#특정 사이트의 텍스트 iframe으로 되어 있는 에디터에 글쓰기

from selenium import webdriver
import time as tt
import random
from datetime import date
from datetime import time
from datetime import datetime

#셋업
driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
driver.set_page_load_timeout(30)

#접속한다.
driver.get("특정사이트")
driver.implicitly_wait(30)

#입력하기 클릭
driver.find_element_by_id("Button2").click()

tt.sleep(3)

#알림창 취소 버튼 누름
alert = driver.switch_to_alert()
alert.dismiss()

tt.sleep(3)


#에디터 찾아, hello 입력
driver.switch_to_frame(0)
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_xpath("/html/body").send_keys("hello")

tt.sleep(3)	

#종료
driver.quit()




