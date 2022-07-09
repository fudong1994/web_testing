# 使用selenium
from selenium import webdriver

# 得到一个浏览器对象
browser = webdriver.Chrome()

# 打开一个网页
url = 'http://www.douban.com'
browser.get(url)

print(browser.title)
print(browser.current_url)
print(browser.page_source)

# # 刷新页面
# browser.refresh()
#
# # 访问一个另外的网址
# browser.get('http://www.baidu.com')
#
# # back:回退
# browser.back()  # 豆瓣
#
# # forward:前进
# browser.forward()  # 百度
#
# # 最小化
# browser.minimize_window()
#
# # 最大化
# browser.maximize_window()
#
# # 全屏
# # browser.fullscreen_window()
#
# # 固定尺寸
# browser.set_window_size(400, 300)
#
# # 关闭标签页(当前页面)
# browser.close()

# 关闭浏览器
browser.quit()