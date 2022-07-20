"""
@Time : 2022/7/20 0020  20:32
@File : d4_select
@Project : web_testing
"""
import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('D:\pythonworkspace\web_testing\第5课：ui操作\select.html')

# 点击 yuz
driver.find_element('xpath', '//option[text()="yuz"]').click()
time.sleep(3)

# 另外封装的一种方式
# 先找到 select 元素，再把元素对象传入 Select
s = driver.find_element('id', 'myselect')
s_obj = Select(s)
s_obj.select_by_visible_text('yuz')
# option value 属性选择
s_obj.select_by_value('y')
# 通过索引
s_obj.select_by_index(2)

driver.quit()
