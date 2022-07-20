"""
@Time : 2022/7/20 0020  20:56
@File : d5_键盘输入
@Project : web_testing
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')

# 执行js指令
js_code = 'return document'
driver.execute_script(js_code)

# 有哪一些指令在 selenium 中不存在
# 1、
el = driver.find_element()
el.get_attribute('href')
# el.set_attribute()

driver.quit()
