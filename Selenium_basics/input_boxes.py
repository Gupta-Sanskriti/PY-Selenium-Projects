# working with the input boxes
from selenium import webdriver
from selenium.webdriver.common.by import By

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")

# 1. how to find how many input boxes present in web pages
ele = driver.find_elements(By.CLASS_NAME,"_2hvTZ")
print(len(ele))

# 2. how to provide value into text box 
# 3. how to get the status

