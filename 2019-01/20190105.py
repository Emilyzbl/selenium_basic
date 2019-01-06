from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://39.107.96.138:3000/signin')

# 用户名
driver.find_element_by_xpath('//*[@id="name"]').send_keys('user1')
# 密码
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('123456')
# 登录
driver.find_element_by_xpath('//*[@type="submit"]').click()
# 发布话题
driver.find_element_by_xpath('//*[@id="create_topic_btn"]').click()
# “选择板块” 下拉列表 
driver.find_element_by_xpath('//*[@id="tab-value"]').click()
# 下拉列表 第二个元素
driver.find_element_by_xpath('//*[@id="tab-value"]/option[2]').click()

# 标题
driver.find_element_by_xpath('//*[@id="title"]').send_keys('20190105测试1，标题')
# 内容
content = driver.find_element_by_xpath('//*[@class="CodeMirror-scroll"]')
content.click()

action = ActionChains(driver)
action.move_to_element(content)
action.send_keys('20190105测试1，内容')

# 在文本输入里面模拟快捷键 Ctrl + b 操作 
driver.find_element_by_xpath('//*[@class="eicon-bold"]').click()

action.perform()



