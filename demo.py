#引入selenium库文件

# 创建Chrome浏览器实例

# 定义一个函数 Param (url,selector,keyword)
# 能够调用， 用 bing 和 百度 搜索


from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome()

def getFirst(url,selector,keyword,imgname):
    driver.get(url)
    if selector == 'kw':
        driver.find_element_by_id('kw').send_keys(keyword)
    driver.save_screenshot('./'+imgname)

url = 'http://www.baidu.com'
key = 'Hello Word'
date = datetime.datetime.now()
imgname = date.strftime('%Y%m%d%H%M%S') + '.png'
getFirst(url,'kw',key,imgname)

time.sleep(5)
driver.quit()

# import datetime as date
# aa = date.datetime.now()
# print(aa)
# bb = date.datetime.now().strftime('%Y%m%d%H%M%S')
# print(bb)
# cc = date.datetime.now().strftime('%Y%m%d%H%M%S') + '.png'
# print(cc)

