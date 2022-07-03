# 使用selenium
from selenium import webdriver

# 得到一个浏览器对象
browser = webdriver.Chrome()

# 打开一个网页
url = 'http://www.douban.com'
browser.get(url)
