from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://result.npgc.in/Default.aspx?ExaminationSession=JUNE-2020")

rollno_feild = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtRollNo")
# rollno_feild.send_keys("")    #enter rollNo. to enter into input feild
# driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnShowResult").click()
# looping up the roll no
# for i in range(217557,218586,1):
#     rollno_feild.clear()
#     rollno_feild.send_keys(i)
#     driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnShowResult").click()
#     time.sleep(5)
#     name = driver.find_element_by_id("ContentPlaceHolder1_lblStudentName").text
#     # print(name.is_enabled())
#     if name == "":    # enter the name of the person where you want to stop the loop
#         break
#     else:
#         driver.back()
#         continue

while True:
    i = 217557
    # rollno_feild.clear()
    rollno_feild.send_keys(i)
    driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnShowResult").click()
    time.sleep(5)
    name = driver.find_element_by_id("ContentPlaceHolder1_lblStudentName").text
    # print(name.is_enabled()) 
    if name == "SANSKRITI GUPTA":
        break
    else:
        driver.back()
        time.sleep(5)
        # rollno_feild.clear()

    i = i +1


        
