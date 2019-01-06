from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

# driver.find_element_by_id('kw').send_keys('通过ID定位元素')
# driver.find_element_by_name('wd').send_keys('通过Name定位元素')

# driver.find_element_by_css_selector('#kw').send_keys('通过CSS定位元素')
# 通过css属性，调click方法
# driver.find_element_by_css_selector('a[name="tj_trnews"]').click()

# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('通过xpath定位元素')
# 通过css属性，调click方法
# driver.find_element_by_css_selector('span[class="soutu-btn"]').click()
# 上传文件 
# driver.find_element_by_css_selector('input[type="file"]').send_keys('D://zblWork//selenium_basic//20181225223101.png')
# driver.find_element_by_css_selector('input[type="file"]').send_keys(r'D:\zblWork\selenium_basic\20181225223101.png')


# 
# selenium获取网页标题、文本、添加判断
# 
print(driver.title)    #打印网页标题

assert 'google' not in driver.title

driver.find_element_by_id('kw').send_keys('Hello World')
driver.find_element_by_id('su').click()

time.sleep(2)    #等待2秒

# 拿到content_left 文本值
result = driver.find_element_by_id('content_left').text
print(result)

assert "Hello World" in result











