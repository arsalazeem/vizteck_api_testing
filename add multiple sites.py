from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import init_chrome
import generate_random_values
from selenium.webdriver.support.select import Select






driver=init_chrome.start()


def write(driver,path,keyvalue):
    driver.find_element_by_xpath(path).send_keys(keyvalue)
    return driver

def click(driver,path):
    driver.find_element_by_xpath(path).click()
    return driver


driver.get("http://54.186.118.166:3600/auth/signup-1")
email=generate_random_values.generate_random_email()
print(email)
driver.implicitly_wait(30)
driver=write(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[1]/div/div[1]/input' ,generate_random_values.generate_random_first_name())
driver=write(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[1]/div/div[2]/input' ,generate_random_values.generate_random_first_name())
driver=write(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[2]/div/div/input',email)
driver=write(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[3]/div/div/input' ,"12345678")
driver=write(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[4]/div/div/input' ,"12345678")
driver=write(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[5]/div/div/input' ,generate_random_values.generate_random_first_name())
driver=click(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[6]/div/div/div[1]/input')
driver=click(driver,'//*[@id="root"]/div/div[2]/div/div/form/div[8]/div/div[2]/button')

#second step
# my_select.select_by_index(1)
#second step ends

