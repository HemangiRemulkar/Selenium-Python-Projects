from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")
driver.refresh()
print("Page refreshed")
driver.back()
time.sleep(2)
print("Navigated back")
driver.forward()
time.sleep(1)
print("Navigated forward")
time.sleep(5)