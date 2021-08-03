from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://www.expedia.com")

driver.find_element(By.ID,"tab-flight-tab-hp").click()
driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("SFO")
time.sleep(2)
