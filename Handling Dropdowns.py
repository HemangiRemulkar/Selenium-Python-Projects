from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown= Select(driver.find_element(By.XPATH,'/html/body/div[2]/div/div/select'))
dropdown.select_by_value('2')
time.sleep(5)