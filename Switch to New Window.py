from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")
firstTabTitle=driver.title

driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])
driver.get("https://bugbug.io/blog/testing-frameworks/best-selenium-practice-websites/")
secondTabTitle=driver.title
print("Second tab title:" + secondTabTitle)

driver.switch_to.window(driver.window_handles[0])

print("First tab title:" + firstTabTitle)