from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.douban.com')

# 面试题：8种定位元素的方式
# driver.find_element_by_class_name()
# driver.find_element_by_id()
# driver.find_element_by_name()
# driver.find_element_by_xpath()
# driver.find_element_by_link_text()
# driver.find_element_by_css_selector()
# driver.find_element_by_tag_name()
# driver.find_element_by_partial_link_text()

# elem 是一个叫做 WebElement 的对象
elem = driver.find_element_by_name('q')
print(elem)

# 获取标签名
print(elem.tag_name)

# 属性、方法
print(elem.send_keys('王者荣耀'))
print(elem.parent)

driver.quit()
# 第二道面试题：find_element和find_elements的区别
