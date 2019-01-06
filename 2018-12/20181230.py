# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')

# # id定位
# driver.find_element_by_id('kw').send_keys('Hello World')
# # name定位
# driver.find_element_by_name('wd').send_keys('Hello World')
# # css定位
# driver.find_element_by_css_selector('#kw').send_keys('Hello World')
# driver.find_element_by_css_selector('a[name="tj_trnews"]').click()
# # xpath定位
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('Hello World')
# # class name定位
# driver.find_element_by_class_name('s_ipt').send_keys('Hello World')
# # 1、a标签 超链接   2、拿到的是a标签的文本，文本必须唯一
# driver.find_element_by_link_text('新闻').click()
# # 所有超链接中，带有“新”的链接
# driver.find_element_by_partial_link_text('新').click()



# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# # 自动上传文件
# driver.find_element_by_css_selector('span[class="soutu-btn"]').click()
# driver.find_element_by_css_selector('input[type="file"]').send_keys(r'D:\zblWork\selenium_basic\test.jpg')



# from selenium import webdriver
# from time
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')

# # 打印标题
# print(driver.title)
# # 断言 google 不包含在标题中
# assert "google" not in driver.title

# # 搜索 Hello World
# driver.find_element_by_id('kw').send_keys('Hello World')
# driver.find_element_by_id('su').click()

# # 等待2秒
# time.sleep(2)

# # 将搜索的值打印出来
# result = driver.find_element_by_id('content').text
# print(result)

# # 结果中包含 Hello World
# assert "Hello World" in result





# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class BaiDuSearch(unittest.TestCase):
#     # 固定方法，每个方法执行之前，都会执行setUp
#     def setUp(self):
#         # 打开浏览器
#         self.driver = webdriver.Chrome()
    
#     # 测试方法必须以 test 为首
#     def test_baidu_search(self):
#         driver = self.driver
#         driver.get('http://www.baidu.com')
#         driver.find_element_by_id('kw').send_keys('Hello World')
#         # 通过快捷键执行Enter操作
#         driver.find_element_by_id('kw').send_keys(Keys.ENTER)

#     def test_bing_search(self):
#         pass

#     # 固定方法，每个test方法执行完后，都会执行tearDown
#     def tearDown(self):
#         # 关闭浏览器
#         self.driver.quit()

# # 自动执行 unittest 中的方法
# if __name__ == "__main__":
#     unittest.main()





import unittest
import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class Cnode(unittest.TestCase):
    def setUp(self):
        self.Url = 'http://39.107.96.138:3000'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
        # 登录用户
        self.driver.find_element_by_css_selector('a[href="/signin"]').click()
        # 输入用户名
        self.driver.find_element_by_id('name').send_keys('user1')
        # 输入密码
        self.driver.find_element_by_id('pass').send_keys('123456')
        # 点击 登录 按钮
        self.driver.find_element_by_css_selector('input[type="submit"]').click()

    def test_post_topic(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/topic/create')
        driver.find_element_by_id('tab-value').click()
        driver.find_element_by_css_selector('[value="share"]').click()
        driver.find_element_by_id('title').send_keys('selenium帖子')
        
        content = driver.find_element_by_class_name('CodeMirror-scroll')
        content.click()

        ActionChains(driver).move_to_element(content).send_keys('selenium代码测试').perform()
        time.sleep(3)
    
    def tearDown(self):
        # 获取当前时间
        date = datetime.datetime.now()
        # 将当前时间转成字符串（年月日时分秒毫秒）
        strDate = date.strftime('%Y%m%d%H%M%S%f')
        # 保存图片
        self.driver.save_screenshot('./' + strDate + '.png')
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    



