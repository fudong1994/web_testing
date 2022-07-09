"""
@Time : 2022/7/9 0009  16:28
@File : d1_等待
@Project : web_testing
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()

# 设置隐性等待，单位是 s(秒)
driver.implicitly_wait(10)

driver.get("http:www.baidu.com")

# 查找kw元素
elem = driver.find_element_by_id("kw")

elem.send_keys("显卡")
elem.submit()

# 查找京东
try:
    driver.find_element_by_xpath('//span[text()="京东"]').click()
except Exception as e:
    print(e)
    print("元素不存在，请检查")
    driver.quit()
else:
    # 等待新页面出现
    time.sleep(5)

    # 现在打开的所有的窗口句柄
    print(driver.window_handles)

    # 打印现在的窗口句柄
    print(driver.current_window_handle)

    # 切换
    # 窗口的句柄传进去
    driver.switch_to.window(driver.window_handles[-1])  # -1 表示选择最后一个窗口

    # 打印切换后的窗口句柄
    print(driver.current_window_handle)

    # 打印标题
    print(driver.title)

    # 关闭浏览器
    driver.quit()
