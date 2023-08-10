from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
drive1 = webdriver.Chrome()
drive1.get("https://www.google.co.il")
search1 = drive1.find_element("id", "APjFqb")
search1.send_keys("ak47")
search1.send_keys(Keys.ENTER)
search1.find_element("xpath", "//*[@id=\"rso\"]/div[1]/div/div/div[1]/div/a/h3/span").click()


# search2 = search1.find_element("XPath", "//*[@id=\"rso\"]/div[1]/div/div/div/div[1]/div/div/div[1]/div/a")
# search2.click()
sleep(60)