from selenium import webdriver
import xlwt
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get('https://s.weibo.com/')

driver.find_element_by_css_selector('div[class="search-input"] > input[type="text"]').send_keys('web自动化')
driver.find_element_by_xpath('//*[@class="s-btn-b"]').click()

driver.find_element_by_link_text('高级搜索').click()
driver.find_element_by_xpath('//*[@for="radio03"]').click()
driver.find_element_by_link_text('搜索微博').click()

ul = driver.find_element_by_xpath('//*[@class="s-scroll"]/ul')
# lis = ul.find_elements_by_xpath('li')
# ul = driver.find_element_by_css_selector('ul[class="s-scroll"]')
liNum = ul.find_elements_by_xpath('li')
print('li个数：'+liNum)

eles = driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')
# print(len(eles))

# 新建一个Excel
excel = xlwt.Workbook()
sheet = excel.add_sheet('测试Sheet')
sheet.write(0,0,'标题')
sheet.write(0,1,'发送人')
sheet.write(0,2,'发布时间')
sheet.write(0,3,'来源')
sheet.write(0,4,'收藏数')
sheet.write(0,5,'转发数')
sheet.write(0,6,'评论数')
sheet.write(0,7,'点赞数')

i = 0
# todo 找到每个微博中的 标题，发送人，发布时间，来源，收藏数，转发数，评论数，点赞数
for aa in eles :
    # 标题
    a1 = aa.find_element_by_xpath('.//*[@node-type="feed_list_content"]').text
    # 发送人
    a2 = aa.find_element_by_xpath('.//*[@class="name"]').text
    # 发布时间
    a3 = aa.find_element_by_css_selector('p[class="from"] > a:nth-child(1)').text
    # 来源
    a4 = aa.find_element_by_xpath('.//*[@rel="nofollow"]').text
    # 收藏数
    a5 = aa.find_element_by_css_selector('div[class="card-act"] > ul > li:nth-child(1)').text
    a51 = a5.split('收藏')[1]
    # 转发数
    a6 = aa.find_element_by_css_selector('div[class="card-act"] > ul > li:nth-child(2)').text
    a61 = a6.split('转发')[1]
    # 评论数
    a7 = aa.find_element_by_css_selector('div[class="card-act"] > ul > li:nth-child(3)').text
    a71 = a7.split('评论')[1]
    # 点赞数
    a8 = aa.find_element_by_xpath('.//*[@title="赞"]').text

    i += 1
    sheet.write(i,0,a1)
    sheet.write(i,1,a2)
    sheet.write(i,2,a3)
    sheet.write(i,3,a4)
    sheet.write(i,4,a51)
    sheet.write(i,5,a61)
    sheet.write(i,6,a71)
    sheet.write(i,7,a8)

    # # print(type(i+1),'999',len(eles))
    # if (i+1) == len(eles):
    #     # 点击 下一页
    #     driver.find_element_by_css_selector('div[class="m-page"] > div > a:nth-child(2)').click()   

# 将数据保存到 Excel 中
excel.save('20190111测试.xls')

