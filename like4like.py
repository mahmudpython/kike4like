import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.like4like.org/login/")
# print(input("Enter Login 01:"))
username = driver.find_element(By.XPATH, "//input[@id='username']").send_keys("mahmud3908")
password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("NbsDCl59")
login_button = driver.find_element(By.XPATH, "//span[@class='button medium orange cursor']").click()
# print(input("Enter Login 02:"))
driver.implicitly_wait(5)
time.sleep(2)
driver.get("https://www.like4like.org/earn-credits.php")
print(input("Enter Login 03:"))
driver.implicitly_wait(4)
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
print(input("Enter Login 04:"))

driver.find_element(By.XPATH, '//div[@role="button" and @data-testid="confirmationSheetConfirm').click()

