'''
selenium 执行 JavaScript 语法
'''

from selenium import webdriver
driver = webdriver.Chrome()

# 
js = 'document.querySelector("#local_news > div.column-title-home > div").scrollIntoView()'
driver.get('http://news.baidu.com')
# 执行 JavaScript 
driver.execute_script(js)

