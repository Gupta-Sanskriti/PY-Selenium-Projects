from selenium import webdriver
from selenium.webdriver.common.by import By

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get(r"C:\Users\Sanskriti\Desktop\selenium_practice\sel_prac\tables.html")

rows = len(driver.find_elements(By.XPATH,"/html/body/table/tbody/tr"))
cols = len(driver.find_elements(By.XPATH,"/html/body/table/tbody/tr[1]/td"))

print(rows)
print(cols)
print("PRODUCT     PRICE")

for r in range (2,rows+1):
    for c in range(1,cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value,end="          ")
    print()
