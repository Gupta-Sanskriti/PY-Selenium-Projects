from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe" #enter the exact location of chrome driver.
driver = webdriver.Chrome(path)

driver.get("https://web.whatsapp.com/")
driver.fullscreen_window()

time.sleep(15)
# search bar
search_bar = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]").send_keys("Tanu Jio")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[10]/div/div/div[2]/div[1]/div[1]/span/span/span").click()

# person = driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span[@title='Path']")
# person.click()
time.sleep(5)


text_bar = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
# text_bar = driver.find_element_by_class_name("_1awRl copyable-text selectable-text")
msg = "this Message is generated by Selenium"

for i in range(1,11,1):
    text_bar.send_keys(msg)
    text_bar.send_keys(Keys.RETURN)
        

