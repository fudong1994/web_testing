"""
@Time : 2022/7/9 0009  16:28
@File : d1_等待
@Project : web_testing
"""
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# 设置隐性等待，单位是 s(秒)
driver.implicitly_wait(10)

driver.get("http:www.baidu.com")

# 查找kw元素
elem = driver.find_element("id", "kw")

elem.send_keys("显卡")
elem.submit()

# 获取点击之前的所有窗口句柄
all_handles = driver.window_handles

# 查找京东
driver.find_element('xpath', '//span[text()="京东"]').click()

# 显性的等待，等待新窗口出现
wait = WebDriverWait(driver, 2)
wait.until(expected_conditions.new_window_is_opened(all_handles))

# 关闭浏览器
driver.quit()
