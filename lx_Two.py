import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GetBaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu_search(self):
        driver = self.driver
        driver.get('http://www.baidu.com')
        driver.find_element_by_id('kw').send_keys('Hello World')
        driver.find_element_by_id('kw').send_keys(Keys.ENTER)
        time.sleep(3)

    def test_bing_search(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


