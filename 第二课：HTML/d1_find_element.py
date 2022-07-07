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
# 输入
elem.send_keys('王者荣耀')
# 清空输入框的内容
elem.clear()
# 获取到该元素的上一级
print(elem.parent)
# 获取元素的属性
print(elem.get_attribute('maxlength'))

# 第二道面试题：find_element和find_elements的区别
# find_element 得到的是一个 WebElement 的对象，只会返回查到的第一个元素，找不到时会报错:NoSuchElementException
# find_elements 得到的是一个列表，返回所有查询到的元素，找不到时返回一个空列表
elems = driver.find_elements_by_name('q')
print(elem)
print(elems)

# 判断元素是否存在
if driver.find_elements_by_name('w'):
    print("元素存在")
else:
    print("元素不存在")

try:
    driver.find_element_by_name('w')
    print("元素存在")
except:
    print("元素不存在")

