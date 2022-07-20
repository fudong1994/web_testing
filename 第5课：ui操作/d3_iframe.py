"""
@Time : 2022/7/9 0009  19:05
@File : d3_iframe
@Project : web_testing
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=html_select')

iframe = driver.find_element('id', 'iframeResult')

# 等待iframe切换成功(自动完成切换操作)
WebDriverWait(driver, 5).until(expected_conditions.frame_to_be_available_and_switch_to_it(iframe))

# alert 切换
# WebDriverWait(driver, 5).until(expected_conditions.alert_is_present)

elem = driver.find_element_by_xpath("//h1")
print(elem)

# 退回主页面
driver.switch_to.default_content()

# 退回父级iframe
# driver.switch_to.parent_frame()

driver.quit()
