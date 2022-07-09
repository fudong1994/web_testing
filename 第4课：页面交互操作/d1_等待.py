"""
# @Time : 2022/7/9 0009  16:28
# @File : d1_等待
# @Project : web_testing

"""
import time
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

dirver = webdriver.Chrome()

# 设置隐性等待，单位是 s(秒)
# dirver.implicitly_wait(10)

dirver.get("http:www.baidu.com")

elem = dirver.find_element_by_id("kw")
elem.send_keys("阿东")
elem.submit()

# 等待的条件：直到页面的标题中包含“阿东”
# wait...until...title_contains("阿东")

wait = WebDriverWait(dirver, timeout=10, poll_frequency=0.2)
wait.until(expected_conditions.title_contains("阿东"))

print(dirver.title)
dirver.quit()