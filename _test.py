from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://comments-school-1.testkontur.ru/comments/preview/1/default/test")
search_fields = driver.find_element(By.NAME, "")
search_fields.send_keys("")
search_fields.send_keys(Keys.ENTER)

header = driver.find_element(By.TAG_NAME, "h2")
assert header.text == "Превью комментариев"


sleep(10)
driver.close()
