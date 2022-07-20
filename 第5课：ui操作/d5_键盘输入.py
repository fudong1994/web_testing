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
input = driver.find_element('id', 'kw')
input.send_keys('哈哈')

# 方式一：找到百度一下这个按钮，点击元素
# 方式二：
# 如果该元素不在 form 表单下，就不能通过 submit 提交
input.submit()

# 方式三：触发键盘上的 回车键
input.send_keys(Keys.ENTER)
input.send_keys(Keys.CONTROL, Keys.SPACE)

# 传键盘操作
ac = ActionChains(driver)
ac.send_keys(Keys.CONTROL).perform()

driver.quit()
