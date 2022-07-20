"""
@Time : 2022/7/18 0018  20:22
@File : d5_鼠标操作
@Project : web_testing
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(r'D:\pythonworkspace\web_testing\第4课：页面交互操作\alert_demo.html')

# 复杂版
# 初始化 ActionChains:动作链条，
action = ActionChains(driver)
# 定位一个元素
h2 = driver.find_element("xpath", "//h2")
# click 操作
action.click(h2).perform()

time.sleep(5)

# 简单
# h2 = driver.find_element_by_xpath("//h2")
# h2.click()

driver.quit()
