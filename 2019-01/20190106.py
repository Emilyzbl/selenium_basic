# '''
# 获取 Excel 中的内容
# '''
# import xlrd
# # 打开excel
# excel = xlrd.open_workbook('test.xls')
# # 获取第一个sheet页的内容
# sheet = excel.sheet_by_index(0)
# # 循环打印第一个sheet页的内容
# for xd in range(sheet.nrows):
#     print(sheet.row(xd))



# '''
# 查找多个元素
# '''
# from selenium import webdriver
# driver = webdriver.Chrome()

# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=7976e95766c245f28a5955da6e2e5a3e')
# eles = driver.find_elements_by_css_selector('li.gl-item div.p-price')

# for i in range(len(eles)):
#     print(eles[i].text)



# '''
# 将内容写入到 Excel 中
# '''
# from selenium import webdriver
# import xlwt
# driver = webdriver.Chrome()

# driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=7976e95766c245f28a5955da6e2e5a3e')

# # 获取所有价格的元素
# price = driver.find_elements_by_css_selector('li.gl-item div.p-price')
# # 获取所有描述的元素
# desc = driver.find_elements_by_css_selector('div.p-name.p-name-type-2')

# count = len(price)
# # 新建一个Excel
# wd = xlwt.Workbook()
# # 在Excel中新建一个sheet
# sheet = wd.add_sheet('jd手机')

# # 第一行第一列写入 手机
# sheet.write(0,0,'手机')
# # 第一行第二列写入 价格
# sheet.write(0,1,'价格')

# for index in range(count):
#     # 第 index+1 行第1列，写入 描述
#     sheet.write(index+1, 0, desc[index].text)
#     # 第 index+1 行第2列，写入 价格
#     sheet.write(index+1, 1, price[index].text)

# # 将写入的值，保存在Excel中
# wd.save('手机价格一览表.xls')




'''

'''
from selenium import webdriver
driver = webdriver.Chrome()

# 打开手机列表界面
driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=87e62f9909374ed08b15a7cc2d675891')

print('打开第一个手机详细页面之后，浏览器tab页面个数：',len(driver.window_handles))

# 查找页面上的手机列表
jd_li = driver.find_elements_by_css_selector('.gl-item > div >div.p-img > a:nth-child(1)')
print(len(jd_li))
cnt = len(jd_li)
for i in range(cnt) :
    jd_li[i].click()
    # 获取所有的浏览器窗口
    allwindows = driver.window_handles
    # 切换到第二个新打开的浏览器窗口
    driver.switch_to.window(allwindows[1])
    # price = driver.find_element_by_css_selector('span.p-price > span.price').text
    # print(price)

    # 关闭第2个浏览器窗口
    driver.close()
    # 切换到第一个浏览器窗口
    driver.switch_to.window(allwindows[0])

