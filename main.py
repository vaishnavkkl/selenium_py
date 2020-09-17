
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#basic commands
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in")
# print(driver.title)
# driver.find_element_by_xpath("//*[@id='nav-cart']").click()
#
# time.sleep(5)
# driver.close() #close current tab
# #driver.quit() [close the whole tab]

#navigation commands

# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in")
# print(driver.title)
#
# driver.get("https://www.facebook.in")
# print(driver.title)
# driver.back()#back navigation
# driver.forward()# forward navigation


#conditional commands

# driver = webdriver.Chrome()
#
# driver.get("https://www.gmail.com")
# einput = driver.find_element_by_id("identifierId")
# einput.send_keys("vaishnav.trv17it057@gecbh.ac.in")
# print(einput.is_displayed()) #return true or false based on elements status
# print(einput.is_enabled())  #return true or false # is_selected to check the radio button
# time.sleep(3)
# driver.find_element_by_id("identifierNext").click()
# time.sleep(5)
# driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("V@ishnav@123")
# driver.find_element_by_id("passwordNext").click()



# explicit wait commands (work based on condition)

driver = webdriver.Chrome()
driver.get("https://www.expedia.com/?pwaLob=wizard-flight-pwa")
time.sleep(13)
des = driver.find_element_by_class_name("uitk-faux-input").send_keys("NYC")


wait = WebDriverWait(driver, 10)

wait.until(EC.url_changes(driver.find_element_by_id("homePage")))

driver.find_element_by_id("mad-t2d-form-input").send_keys("90909090")
