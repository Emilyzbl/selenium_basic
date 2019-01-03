import xlrd
# 打开excel
excel = xlrd.open_workbook('test.xls')
# 获取第一个sheet页的内容
sheet = excel.sheet_by_index(0)
# 循环打印第一个sheet页的内容
for xd in range(sheet.nrows):
    print(sheet.row(xd))



