import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.like4like.org/login/")

# print(input("Enter Login :"))

username = driver.find_element(By.XPATH, "//input[@id='username']").send_keys("mahmud3908")
password = driver.find_element(By.XPATH, "//input[@id='password']").send_keys("NbsDCl59")
login_button = driver.find_element(By.XPATH, "//span[@class='button medium orange cursor']").click()


# print(input("Enter Login :"))
driver.implicitly_wait(3)
time.sleep(1)
driver.get("https://www.like4like.org/user/earn-facebook.php")

# print(input("Enter Login :"))
driver.implicitly_wait(4)
time.sleep(4)
facebook_like = driver.find_element(By.XPATH, "//div[@id='likebutton45043']")
print(facebook_like)

print(input("Enter Login :"))

