from selenium import webdriver
from selenium.webdriver.support.ui import Select


path = r"C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get(r"C:\Users\Sanskriti\Desktop\selenium_practice\sel_prac\dropdown.html")

element = driver.find_element_by_id("dropdown")
#   SELECT AN OPTION
drp = Select(element)

# select by visible text
# print(drp.select_by_visible_text("monday"))

# select by index
# drp.select_by_index(1)

# select by value
# drp.select_by_value("wednesday")

# CAPTURE OPTION FROM DROPDOWN 
# count no. of options 
# print(len(drp.options))

# capture options and prin them all
all_options = drp.options
for option in all_options:
    print(option.text)


