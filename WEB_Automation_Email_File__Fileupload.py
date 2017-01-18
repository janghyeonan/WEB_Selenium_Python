#-*- coding:utf-8 -*-

##import 묶음
import glob, os
import time as tt
from datetime import date
from datetime import time
from datetime import datetime
from selenium import webdriver
import datetime
import selenium

# 이메일로 온 내용 중 특정 메일을 검색하여, 첨부파일을 다운로드 받은 후 해당 첨부파일을 데이터 수집하는 웹페이지에
# 자동으로 파일 업로드를 한다.


#파일 리스트 전역변수
filelist = []

driver = webdriver.Chrome("D:\selenium\chromedriver.exe")

#함수리스트

#웹 드라이브 열기
def web_open(urll):        
    driver.set_page_load_timeout(30)
    driver.get(urll)
    driver.maximize_window()
    driver.implicitly_wait(30)

#오늘의 날짜 검색 6자리
def today_6day():
    global result
    today = datetime.date.today()
    kk = today.year
    mm = today.month
    nn = today.day -1

    kk = str(kk).replace("201", "1")

    if len(str(mm)) < 2 :
        mm = "0" + str(mm)
    
    if len(str(nn)) < 2 :
        nn = "0" + str(nn)

    result = str(kk) + str(mm) + str(nn)    

#해당 폴더의 파일을 찾아 전체 파일명 얻는(리스트에 넣음)
def find_file():        
    target_dir = r'C:/Users/ajh910/Downloads/'
    for file in glob.glob(target_dir + "%s*.xlsx" %result):
        filelist.append(file)


#로그파일 만듬
def save_log(message):
    with open(r"D:/log/"+str(datetime.datetime.now())[:19]+"_log_fileupload.txt", 'a') as f:        
        f.write(str(datetime.datetime.now())[:19]+" - " + message +"\n" )
    print(str(datetime.datetime.now())[:19]+" - " + message)

#함수 끝



#시작로그
save_log("작업시작")

#메일 사이트 접속
web_open("http://메일 사이트")
save_log("접속 완료")

#스마일넷 아이디 비밀번호 입력 / 로그인
driver.find_element_by_id("txtUserName").send_keys("아이디")
driver.find_element_by_id("txtPassword").send_keys("비밀번호!")
driver.find_element_by_css_selector("#imgLogin").click()
save_log("로그인 완료")
tt.sleep(3)

#검색창에 미처리 내역 넣고, 검색 버튼 누르기
driver.switch_to_frame(0)
ab = driver.find_element_by_css_selector('#txtSearchWord')
ab.send_keys("미처리 내역")
driver.find_element_by_css_selector('#divSearch > fieldset > span.buttonSearchB').click()
tt.sleep(3)
driver.find_element_by_css_selector('#listView_0_6 > a').click()
save_log("미처리 내역 검색창에 입력, 검색 버튼 누르기 완료")
tt.sleep(5)

# 검색 내용 중 첫번째 클릭 후 새로운 윈도우 창으로 이동 후 첨부파일 누르기
driver.switch_to_window(driver.window_handles[1])
driver.find_element_by_css_selector('#divAttach > a').click()
save_log("이메일 첨부파일 다운로드  완료")
tt.sleep(5)

#브라우저 종료
driver.quit()
save_log("브라우저 종료")

#날짜 검색 미리 해두기
today_6day()
save_log("날짜 추출 완료")

#얻은 날짜 값으로 다운로드된 파일명 찾기
find_file()
save_log("파일명 얻기 완료")

#업로드용 페이지열기
driver = webdriver.Chrome("D:\selenium\chromedriver.exe")
web_open("http://localhost/파일 업로드 주소")
save_log("cs파일 업로드 페이지  접속 완료")

#파일 업로드 하기
tt.sleep(5)
driver.find_element_by_id("FileUpload1").send_keys(filelist[0])
tt.sleep(10)
driver.find_element_by_css_selector('#Button1').click()
save_log("파일 업로드 완료")

#종료 카운트 다운
print("10후 종료")
tt.sleep(10)


#종료
driver.quit()
save_log("종료")
