"""
@Time : 2022/7/9 0009  19:05
@File : d3_iframe
@Project : web_testing
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.w3school.com.cn/tiy/t.asp?f=html_select')

# 如果想找一个 iframe 当中的元素，不能直接查找，而是先要进入到 iframe 当中
# 提供 iframe 的标识：index,name,iframe Webelement
iframe = driver.find_element_by_id('iframeResult')

# 切换到iframe窗口
# driver.switch_to.frame(0) # 下标，0代表第一个iframe窗口
# driver.switch_to.frame('iframeResult') # name元素
driver.switch_to.frame(iframe)  # iframe 的 element对象

elem = driver.find_element_by_xpath("//h1")
print(elem)

driver.quit()
