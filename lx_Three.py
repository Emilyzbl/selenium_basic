import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 用于定位的常用的元素属性：
# id    
# name    
# class name  
# tag name   
# link text  
# partial link text    
# xpath   
# css selector
        
class GetBaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu_search(self):
        driver = self.driver
        driver.get('https://www.baidu.com')

        # driver.find_element_by_id('kw')
        # driver.find_element_by_name('wd')
        # driver.find_element_by_xpath('//*[@id="kw"]')
        # driver.find_element_by_link_text('新闻')
        # driver.find_element_by_partial_link_text('新')
        # driver.find_elements_by_tag_name('')
        # driver.find_element_by_class_name('s_ipt')
        # driver.find_element_by_css_selector('')

        # driver.find_element_by_id('kw').send_keys(Keys.ENTER)

    def test_bing_search(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


