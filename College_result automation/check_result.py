from selenium import webdriver
from selenium.webdriver import ActionChains as AC
from selenium.webdriver.common.by import By
import time

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("http://result.npgc.in/Default.aspx?ExaminationSession=JUNE-2020")




for i in range (1,40):
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_txtRollNo']").clear()
    driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_txtRollNo']").send_keys(218565+i)
    driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_btnShowResult']").click()
    student_name = driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_lblStudentName']")
    # error = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table/tbody/tr[7]/td/span")
    if student_name.text != "": #enter the name of the student where you want to stop the loop
        time.sleep(1)
        driver.back()
        continue

    # if error.text == "No Record Found. / Result not yet Declared.":
    #     driver.find_element(By.XPATH,"//*[@id='ContentPlaceHolder1_txtRollNo']").clear()
    #     continue
    
