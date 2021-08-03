from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.maximize_window() #maximize the window

#opens url
driver.get("https://www.travolook.in/?gclid=CjwKCAiAo5qABhBdEiwAOtGmbq35Stw9GTUmPPERqrFAGGNHYIRmm4Dpxfbf4qNp7oXPrR3fe2ubJxoCqwIQAvD_BwE")

time.sleep(3)
# get the basic value into variable
ele_from = driver.find_element(By.XPATH,"//*[@id='flying_from_N']")
ele_from_search = driver.find_element(By.XPATH,"//*[@class='fly-from-input']")
element_from = driver.find_element(By.XPATH,"/html/body/div[4]/ul/li")
ele_to = driver.find_element(By.XPATH,"//*[@id='flying_to_N']")
ele_departure = driver.find_element(By.XPATH,"//*[@id='Fly_depdate_val']")
ele_return = driver.find_element(By.XPATH,"//*[@id='Fly_retdate_val']")
ele_traveller = driver.find_element(By.XPATH,"//*[@id='adult_div']/span")
search_btn = driver.find_element(By.XPATH,"//*[@id='adult_div']/span")


# from fill
ele_from.click().ele_from_search.click().send_keys("lucknow").element_from.click()  

