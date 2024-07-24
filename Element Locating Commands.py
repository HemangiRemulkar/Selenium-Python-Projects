from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://formy-project.herokuapp.com/buttons")
element_primary=driver.find_element(By.CLASS_NAME, 'btn-primary')
element_primary.click()
print("element_primary clicked by CLASS_NAME")
element_primary1=driver.find_element(By.CSS_SELECTOR,'body > div:nth-child(1) > form:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
element_primary1.click()
print("element_primary clicked by CSS_SELECTOR")
element_success=driver.find_element(By.XPATH,'/html/body/div/form/div[1]/div/div/button[2]')
element_success.click()
print("element_success clicked by XPATH")
element_link=driver.find_element(By.PARTIAL_LINK_TEXT,'Link')
element_link.click()
print("element_success clicked by Link")


