'''
百度识别验证码
'''
# from selenium import webdriver
# import base64
# import requests

# driver = webdriver.Chrome() 
# driver.get('https://persons.shgjj.com/')


# image = driver.find_element_by_id('img1')

# image.screenshot('./01.png')

# f = open(r'./01.png', 'rb')
# # 参数image：图像base64编码
# img = base64.b64encode(f.read())

# import requests

# url = "https://aip.baidubce.com/oauth/2.0/token"

# querystring = {"grant_type":"client_credentials","client_id":"1RQYVnqvNBIPoxFtzr68mWzz","client_secret":"NcQfFTMwmNyayuQiLsugfyiP05nPmnKT"}

# payload = ""
# headers = {
#     'cache-control': "no-cache",
#     'Postman-Token': "53654ba8-1fa5-419f-9cf5-d585dd302b5d"
#     }

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# # print(response.json())

# data = response.json()
# print (data['access_token'])

# access_token = data['access_token']

# url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"

# querystring = {"access_token":access_token}

# payload = {"image": img}
# headers = {
#     'Content-Type': "application/x-www-form-urlencoded",
#     'cache-control': "no-cache"
#     }

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

# print(response.json())

# checkData = response.json()

# num = checkData['words_result'][0]['words']

# driver.find_element_by_id('imagecode1').send_keys(num)





'''

'''

# from selenium import webdriver
# from os import path

# #定义截图存储的路径
# d = path.dirname(__file__)
# index = path.join(d,'index.png')
# image = path.join(d,'image.png')

# driver = webdriver.Chrome()

# driver.get("https://www.baidu.com/")

# #百度首页截图保存的路径名
# driver.save_screenshot('./index.png')

# driver.find_element_by_class_name('soutu-btn').click()






'''
模拟快捷键
'''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


# driver = webdriver.Chrome() 

# driver.get('http://39.107.96.138:3000/signin')
# driver.find_element_by_id('name').send_keys('user1')
# driver.find_element_by_id('pass').send_keys('123456')
# driver.find_element_by_css_selector('.span-primary').click()

# driver.get('http://39.107.96.138:3000/topic/create')

# input_content = driver.find_element_by_css_selector('.CodeMirror-lines')
# input_content.click()

# action = ActionChains(driver)

# action.move_to_element(input_content).send_keys('abc')

# action.key_down(Keys.CONTROL)
# action.send_keys('a')
# action.key_up(Keys.CONTROL)

# action.key_down(Keys.CONTROL)
# action.send_keys('b')
# action.key_up(Keys.CONTROL)


# # perform()
# action.perform()




'''
iframe 切换
'''
# from selenium import webdriver
# driver = webdriver.Chrome()

# driver.get('https://login.anjuke.com/login/form')

# driver.switch_to_frame('iframeLoginIfm')

# driver.find_element_by_id('pwdTab').click()

# driver.find_element_by_id('pwdUserNameIpt').send_keys('12345')

# driver.find_element_by_id('pwdIpt').send_keys('sddsds')




'''
alert窗口操作
'''
# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
# driver = webdriver.Chrome()

# driver.get('http://39.107.96.138:3000/signin')
# driver.find_element_by_id('name').send_keys('user1')
# driver.find_element_by_id('pass').send_keys('123456')
# driver.find_element_by_css_selector('.span-primary').click()

# driver.get('http://39.107.96.138:3000/user/user1')

# driver.find_element_by_class_name('topic_title').click()

# driver.find_element_by_css_selector('i.fa.fa-lg.fa-trash').click()

# print(Alert(driver).text)
# # 取消
# Alert(driver).dismiss()
# # 确定
# Alert(driver).accept()



'''
执行JavaScript脚本
'''
# from selenium import webdriver
# driver = webdriver.Chrome()

# driver.get('https://www.ctrip.com/')
# start_date = '2019-01-20'

# js_script ='document.querySelector("#HD_CheckIn").value = "{}"'.format(start_date)
# # print(js_script)
# driver.execute_script(js_script)

# end_date = '2019-01-22'
# end_script = 'document.querySelector("#HD_CheckOut").value = "{}"'.format(end_date)
# driver.execute_script(end_script)




'''
手机端模拟
'''
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# mobileEmulatio = {"deviceName":'iPad'}
# chrome_options.add_experimental_option('mobileEmulation',mobileEmulatio)
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://www.baidu.com')



# from selenium import webdriver
# import time
# driver = webdriver.Chrome()
# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=e731e1e224b9455fa7b3cfe95151ebf4')
# driver.maximize_window()
# result = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]')
# print(len(result))
# print('打开的页面数',len(driver.window_handles))
# for index in range(len(result)):
# result = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]')
# result[index].click()
# allwindows = driver.window_handles
# driver.switch_to.window(allwindows[1])
# time.sleep(2)
# text = driver.find_element_by_css_selector('span.price.J-p-100002332162').text
# print(text)
# driver.close()
# driver.switch_to.window(allwindows[0])
# time.sleep(2)


