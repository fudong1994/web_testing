"""
# @Time : 2022/7/9 0009  16:08
# @File : d1
# @Project : web_testing
"""
from selenium import webdriver
import time

driver = webdriver.Chrome()

# 设置隐性等待，单位是 s(秒)
driver.implicitly_wait(10)

driver.get("http:www.baidu.com")

elem = driver.find_element("id", "kw")
elem.send_keys("阿东")
elem.submit()

# 强制等待
time.sleep(3)
# 隐性等待：只能用来等待元素出现
# 启动浏览器只需要设置一次

print(driver.title)
driver.quit()