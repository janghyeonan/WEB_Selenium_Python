# 특정 사이트 웹 자동화 시도

from selenium import webdriver
import time as tt
import random
from datetime import date
from datetime import time
from datetime import datetime

#팝업 종료 함수1
def popup_close():
    driver.find_element_by_css_selector("#div_popup_20160523 > div.popupFooter > span > a > img").click()
    tt.sleep(2)

#스크린샷 저장 함수
def screen_shot_g():
    today = datetime.now()
    driver.save_screenshot('d:\\python_test\\%s' % today.strftime("%y%m%d%H%M%S") +"_gmspage"+ ".jpg")


#셋업
driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("특정사이트")
driver.maximize_window()
driver.implicitly_wait(30)

#아이디/비밀번호 입력 / 로그인 완료
driver.find_element_by_id("ID").send_keys("아이디")
driver.find_element_by_id("Password").send_keys("비밀번호")
driver.find_element_by_css_selector("#a_login > span").click()
tt.sleep(2)
print("로그인완료")

driver.find_element_by_css_selector("#popupStandard_Date > div.popupMonth_B > div").click()
tt.sleep(2)
driver.find_element_by_css_selector("#popupStandard_Date > div.popupMonth_B > span > a").click()
tt.sleep(2)
print("결재팝업종료")

# 팝업창 끄기
popup_close()
print("브라우저 지원 팝업 종료")

#1~8번째 메뉴 활성화 후 종료 / 메뉴 활성화 시 해당 화면 저장
#동일한 구문 복사/붙여넣기. 다음 파일에서는 for문으로 변경

#첫번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[1]/a").click()
tt.sleep(2)
screen_shot_g()
print("첫번째 메뉴 종료")

#두번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[2]/a").click()
tt.sleep(2)
screen_shot_g()
print("두번째 메뉴 종료")

#세번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[3]/a").click()
tt.sleep(2)
screen_shot_g()
print("세번째 메뉴 종료")

#네번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[4]/a").click()
popup_close()
tt.sleep(2)
screen_shot_g()
print("네번째 메뉴 종료")

#다섯번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[5]/a").click()
tt.sleep(2)
screen_shot_g()
print("다섯번째 메뉴 종료")

#여섯번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[6]/a").click()
tt.sleep(2)
screen_shot_g()
print("여섯번째 메뉴 종료")

#일곱번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[7]/a").click()
tt.sleep(2)
screen_shot_g()
print("일곱번째 메뉴 종료")

#여덜번째 메뉴
driver.find_element_by_xpath("/html/body/div[2]/div[2]/nav/ul/li[8]/a").click()
tt.sleep(2)
screen_shot_g()
print("테스트 끝")

#종료
driver.quit()
