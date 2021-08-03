from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://login.yahoo.com/")

ele = driver.find_element_by_xpath("//*[@id='login-username']")

print("is enabled: ",ele.is_enabled())
print("is displayed: ",ele.is_displayed())
print("is selected: ",ele.is_selected())

