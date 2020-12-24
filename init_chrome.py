from selenium import webdriver
import pdb

# import
import time





def start():
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.maximize_window()
    return driver


