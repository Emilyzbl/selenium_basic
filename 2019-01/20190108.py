from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('http://39.107.96.138:3000/')
login = driver.find_element_by_xpath('//*[@href="/signin"]').click()

driver.find_element_by_xpath('//*[@id="name"]').send_keys('user1')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
driver.find_element_by_xpath('//*[@type="submit"]').click()

driver.find_element_by_xpath('//*[@class="span-success"]').click()

driver.find_element_by_xpath('//*[@id="tab-value"]').click()
driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()

driver.find_element_by_xpath('//*[@id="title"]').send_keys('20190108测试1，标题')

content = driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')
content.click()

action = ActionChains(driver)
action.move_to_element(content)
action.send_keys('20190108测试1，内容')

# 第一种方法：在文本输入里面模拟快捷键 Ctrl + b 操作 
action.key_down(Keys.CONTROL)
action.send_keys('b')
action.key_up(Keys.CONTROL)
# 第二种方法：在文本输入里面模拟快捷键 Ctrl + b 操作 
action.send_keys(Keys.CONTROL,'b')

action.perform()

