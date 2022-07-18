"""
@Time : 2022/7/18 0018  20:36
@File : d6_baidu
@Project : web_testing
"""

import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.baidu.com')

# 找到要移动的元素
setting = driver.find_element_by_xpath('//span[text()="设置"]')

# 鼠标悬停，move_to_element
ac = ActionChains(driver)
ac.move_to_element(setting).perform()

time.sleep(3)

# 找到高级搜索
adv_setting = driver.find_element_by_xpath('//span[text()="高级搜索"]')
adv_setting.click()
# ac.click(adv_setting).perform()

# 链式调用
ac.move_to_element(setting).click(adv_setting).drag_and_drop().context_click().perform()
