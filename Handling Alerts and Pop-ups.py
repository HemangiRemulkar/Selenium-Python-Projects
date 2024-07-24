from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#Alert popup with OK Button
clickForJSAlerts=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/ul/li[1]/button').click()
alert=driver.switch_to.alert
alert.accept()
print("Accepted")

#Alert with OK and Cancel

clickForJSConfirm=driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button').click()
alert=driver.switch_to.alert
time.sleep(2)
alert.accept()
time.sleep(2)
print("Accepted")
time.sleep(5)
clickForJSConfirm1=driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[2]/button').click()
time.sleep(2)
alert=driver.switch_to.alert
time.sleep(2)
alert.dismiss()
print("Declined")

#Enter text with Prompt
clickForJSPrompt=driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
time.sleep(2)
alert = driver.switch_to.alert
time.sleep(2)
alert.send_keys('text')
alert.accept()
time.sleep(5)
print("Text entered")


