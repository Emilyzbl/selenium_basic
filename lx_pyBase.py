# class father:
#     def money(self):
#         print(999999)

# class father2:
#     def factory(self):
#         print('I have factory')



class grandpa:
    def money(self):
        print(100)
    def factory(self):
        print("I have none")

class father(grandpa):
    pass
#     def money(self):
#         print(190000000)
#     def factory(self):
#         print("I have 江南皮革厂")

class father2(grandpa):
    pass
#     def factory(self):
#         print("I have alibaba")
#     def money(self):
#         print("9999991999999999900")

class son(father,father2):
    pass


# john = son()
# john.factory()
# john.money()


# class PlusNum:
#     def plus_int(self,a,b):
#         return a+b

#     def plus_float(self,a,b):
#         return a+b

#     def plus_all(self,a,b,c,d):
#         return self.plus_int(a,b)+self.plus_float(c,d)

# num = PlusNum()
# # print(num.plus_int(3,4))
# # print(num.plus_float(2.1,7.5))
# print(num.plus_all(1,2,3.2,3.4))



# class PlusNum:
#     def plus_int(self,a,b):
#         return a+b

#     def plus_float(self,a,b):
#         return a+b

#     def plus_all(self,a,b,c,d):
#         return self.plus_int(a,b)+self.plus_float(c,d)



# class PlusNum:
#     def plus_int(self,a,b):
#         a = int(a)
#         b = int(b)
#         return a+b
    
#     def plus_float(self,a,b):
#         a = float(a)
#         b = float(b)
#         return a+b
    
#     def plus_all(self,a,b,c,d):
#         return self.plus_int(a,b)+self.plus_float(c,d)
        
    
# num = PlusNum()
# print(num.plus_int(a = 3,b = 4))
# print(num.plus_float(a = 2.1,b = 1.2))
# print(num.plus_all(a = 1,b = 2,c = "1.2",d = "3.4"))



class Xiniu:
    @classmethod
    def runing(cls):
        print('狂奔的犀牛')

# # 类方法调用
# Xiniu.runing()
# # 实例化调用
# aa = Xiniu()
# aa.runing()



# class Run:
#     @staticmethod
#     def have_breakfast():
#         print('eat bread')

# # 类方法调用
# Run.have_breakfast()
# # 实例化调用
# r = Run()
# r.have_breakfast()





# import re
# import requests
# import json

# response =requests.get('https://api.douban.com/v2/book/search?q=%E5%B0%8F%E7%8E%8B%E5%AD%90')

# with open('douban.json','a') as file:
#     file.write(json.dumps(response.json()))



import re
import requests
# import json

response = requests.get('https://api.douban.com/v2/book/search?q=%E5%B0%8F%E7%8E%8B%E5%AD%90')
# aaa = response.content
# print(aaa)
# bbb = response.json()
# print(bbb)

# print(response)
# content = response.text         #获取网页上的内容
# print(content)

# with open('douban.json','w',encoding='utf-8') as file:
#     file.write(content)





# import json
# import requests

# response = requests.get('https://api.douban.com/v2/book/search?q=%E5%B0%8F%E7%8E%8B%E5%AD%90')
# print(type(response.text))
# print(type(response.content))
# print(type(response.json()))
# print(response.json())

# print(str(response.content,'utf-8'))

# import json
# import requests

# response = requests.get('https://api.douban.com/v2/book/search?q=%E5%B0%8F%E7%8E%8B%E5%AD%90')

# print(str(response.content,'utf-8'))
# # print(response.json())





# file = open('douban.json','r',encoding='utf-8')
# string = file.read()
# pattern = re.compile(r'小王子')
# result = pattern.findall(string)
# print(result)

# \d 代表匹配所有数字，{}
# pattern = re.compile(r'\d')        # 找一位数
# pattern = re.compile(r'\d\d')      # 找两位数
# pattern = re.compile(r'\d{1,4}')   # 找1,2,3,4位数，大括号{}中的1代表一位数，4代表4位数
# pattern = re.compile(r'\d{,10}')   # 前面不写，表示取为空 和到10位的数字

#  加号+ 和 大括号() 意思一样
# pattern = re.compile(r'\d{1,}')   #  后面数字不写，表示取出最少出现一位数，最大数无穷大
# pattern = re.compile(r'\d+')      #  +的意思是，对加号前面的数字，匹配一次或多次

#  加号+
# pattern = re.compile(r'\w')      #  \w  数字，字母，下划线，汉字
# pattern = re.compile(r'\w+')     #  \w+ 所有数字，字母，下划线，汉字
# pattern = re.compile(r'\W+')     #  \W+ 匹配所有除数字，字母，下划线，汉字以外，所有内容 
# pattern = re.compile(r'\D+')     #  \D+ 匹配所有非数字的内容

# result = pattern.findall(string)
# print(result)

# file.close()





file = open('douban.json','r',encoding='utf-8')
string = file.read()
# string2 = 'pingan.john.sw@eric.sf.com.cn'
# string2 = 'pingan.johnsw@eric.com,pingansjohnsw@ericxcom,pingan!johnsw@ericxcom'

# pattern = re.compile(r'pingan.johnsw@eric.com')    
# pattern = re.compile(r'.')                         #  .代表匹配所有内容
# pattern = re.compile(r'pingan\.johnsw@eric\.com')    #  \. 将点转义

# string2 = 'pingan.johnsw@eric.com,253453534@qq.com,dolphinsspsf@aliyun.com'
# pattern = re.compile(r'pingan\.johnsw@eric\.com')    #
# pattern = re.compile(r'\w+@\w+\.com')

# string3 = 'chuxiuhong@hit.edu.cn.cf.cnn.dnf'
# pattern = re.compile(r'@\w+.')
# pattern = re.compile(r'@.+?\.')

# result = pattern.findall(string3)

# pattern =re.compile(r'"count":(.*?),')
# result = pattern.findall(string)
# sum = 0
# for i in result:
#     sum += int(i)
# print(sum)
# print(result)

file.close()


import requests
response = requests.get('https://movie.douban.com/top250')
content = response.text
# with open ('douban.txt','w',encoding='utf-8') as ff:
    # ff.write(content)

file = open('douban.txt','r',encoding='utf-8')
string = file.read()

pattern = re.compile(r'src="(.*?)"',re.S)
result = pattern.findall(string)
print(result)
file.close()



