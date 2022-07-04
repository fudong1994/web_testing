from selenium import webdriver


def test_start_selenium():
    # 测试步骤
    driver = webdriver.Chrome()
    url = 'http://www.douban.com'
    driver.get(url)
    # 点点点省略

    # 找到需要操作的元素输入框
    input_el = driver.find_element('xpath', '//*[@id="anony-nav"]/div[3]/form/span[1]/input')
    # 输入内容
    input_el.send_keys("老友记")
    # 提交
    input_el.submit()
    # 断言
    actual = driver.title
    driver.quit()
    assert actual == '搜索: 老友记'
