from selenium import webdriver
driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get('https://s.weibo.com/')

driver.find_element_by_css_selector('div[class="search-input"] > input[type="text"]').send_keys('web自动化')
driver.find_element_by_xpath('//*[@class="s-btn-b"]').click()

driver.find_element_by_link_text('高级搜索').click()
driver.find_element_by_xpath('//*[@for="radio03"]').click()
driver.find_element_by_link_text('搜索微博').click()

# eles = driver.find_elements_by_xpath('//*[@action-type="feed_list_item"]')
eles =driver.find_elements_by_css_selector('div[action-type="feed_list_item"]')
# print(eles)

# for ele in eles:
#     title = ele.find_element_by_css_selector('p[class="txt"]').text
#     username = ele.find_element_by_css_selector('a[class="name"]').text
#     time = ele.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text
#     source = ele.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text
#     coll = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(1)').text
#     coll_num = coll.split('收藏')[1]
#     forward = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(2)').text
#     forward_num = forward.split('转发')[1]
#     comment = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(3)').text
#     comment_num = comment.split('评论')[1]
#     like = ele.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(4)').text
#     # print(title,username,time,coll_num,forward_num,coll_num,like)
#     print('a1：'+title,'a2：'+username,'a3：'+time,'a4：'+coll_num,'a5：'+forward_num,'a6：'+coll_num,'a7：'+like)

# todo 找到每个微博中的 标题，发送人，发布时间，来源，收藏数，转发数，评论数，点赞数
for aa in eles :
    # 标题
    title = aa.find_element_by_css_selector('p[class="txt"]').text
    # 发送人
    username = aa.find_element_by_css_selector('a[class="name"]').text
    # 发布时间
    date = aa.find_element_by_css_selector('p[class="from"]>a:nth-child(1)').text
    # 来源
    laiyuan = aa.find_element_by_xpath('//*[@rel="nofollow"]').text
    # 收藏数
    shoucang = aa.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(1)').text
    sc_num = shoucang.split('收藏')[1]
    # 转发数
    zhuanfa = aa.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(2)').text
    zf_num = zhuanfa.split('转发')[1]
    # 评论数
    pinglun = aa.find_element_by_css_selector('div[class="card-act"]>ul>li:nth-child(3)').text
    pl_num = pinglun.split('评论')[1]
    # 点赞数
    dianzan = aa.find_element_by_xpath('//*[@title="赞"]').text

    print('a1：'+title,'a2：'+username,'a3：'+date,'a4：'+sc_num,'a5：'+zf_num,'a6：'+pl_num,'a7：'+dianzan)

