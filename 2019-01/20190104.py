from selenium import webdriver
import xlwt
driver = webdriver.Chrome()

driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=7976e95766c245f28a5955da6e2e5a3e')

# 获取所有价格的元素
price = driver.find_elements_by_css_selector('li.gl-item div.p-price')
# 获取所有描述的元素
desc = driver.find_elements_by_css_selector('div.p-name.p-name-type-2')

count = len(price)
# 新建一个Excel
wd = xlwt.Workbook()
# 在Excel中新建一个sheet
sheet = wd.add_sheet('jd手机')

# 第一行第一列写入 手机
sheet.write(0,0,'手机')
# 第一行第二列写入 价格
sheet.write(0,1,'价格')

for index in range(count):
    # 第 index+1 行第1列，写入 描述
    sheet.write(index+1, 0, desc[index].text)
    # 第 index+1 行第2列，写入 价格
    sheet.write(index+1, 1, price[index].text)

# 将写入的值，保存在Excel中
wd.save('手机价格一览表.xls')






