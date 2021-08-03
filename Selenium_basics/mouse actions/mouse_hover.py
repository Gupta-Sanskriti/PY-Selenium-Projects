from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("http://npgc.in/")

student_corn = driver.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[7]/a")
downloads = driver.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[7]/ul/li[4]/a")
syllabus = driver.find_element_by_xpath("//*[@id='navbar-collapse']/ul/li[7]/ul/li[4]/ul/li[1]/a")

actions = ActionChains(driver)

actions.move_to_element(student_corn).move_to_element(downloads).move_to_element(syllabus).click().perform()