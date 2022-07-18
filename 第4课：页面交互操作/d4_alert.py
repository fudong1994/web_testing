"""
@Time : 2022/7/18 0018  20:09
@File : d4_alert
@Project : web_testing
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(r'D:\pythonworkspace\web_testing\第4课：页面交互操作\alert_demo.html')

h2 = driver.find_element_by_xpath("//h2")
h2.click()

# 切换到alert,点击确定
my_alert = driver.switch_to.alert
# 确定
my_alert.accept()
# 取消
# my_alert.dismiss()

driver.find_element_by_xpath("//h2")

driver.quit()
