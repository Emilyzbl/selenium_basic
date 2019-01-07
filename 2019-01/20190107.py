import requests,base64
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://persons.shgjj.com/')
time.sleep(2)
# 定位 验证码
image_ele = driver.find_element_by_id('img1')
# 将网站上显示的验证码，保存成图片
image_ele.screenshot('./20190107.png')

# client_id 为百度官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Esrbpi4v4e2kjjrD1Pt15rYk&client_secret=9wKTIulk1iPfS4qj7zWK3o7TXF6S30kN'
# 发送get请求，返回服务器结果
res = requests.get(host)
# 将服务器返回的结果转成json格式
r = res.json() 
print(r)

# 拿到json中的 access_token 字段
access_token = r['access_token']

print(access_token)

# access_token = '#####调用鉴权接口获取的token#####'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'./20190107.png', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
# 上传
imageres = requests.post(url,data=params)  # data=params 上传的数据
image_json = imageres.json()
print(imageres.json())

image_num = image_json['words_result'][0]['words']
# 识别的文本，输入到 验证码文本框
driver.find_element_by_id('imagecode1').send_keys(image_num)



