from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://codepen.io/blink172/pen/vERyxK")

element = driver.find_element_by_xpath("//*[@id='dcCount']")

actions = ActionChains(driver)
time.sleep(5)

actions.double_click(element).click().perform()
