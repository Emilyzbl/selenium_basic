#引入selenium库文件

# 创建Chrome浏览器实例

# 定义一个函数 Param (url,selector,keyword)
# 能够调用， 用 bing 和 百度 搜索


from selenium import webdriver
import time
driver = webdriver.Chrome()

def getFirst(url,selector,keyword):
    driver.get(url)
    if selector == 'kw':
        driver.find_element_by_id('kw').send_keys(keyword)
    driver.save_screenshot('./20181223.png')

url = 'http://www.baidu.com'
key = 'Hello Word'
getFirst(url,'kw',key)

time.sleep(5)
driver.quit()




