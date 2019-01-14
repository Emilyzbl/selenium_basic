'''
Python面向对象01-类和实例的定义
'''
class TestOne:
    def __init__(self,aa,bb,cc):
        self.aa = aa
        self.bb = bb
        self.cc = aa + bb + '@123.com'
        self.dd = cc

    def fullname(self):
        return ('{} {}'.format(self.aa,self.bb))
    
test_1 = TestOne('hello','world',100)
test_2 = TestOne('test','world',200)

# print(test_1)
# print(test_2)

# print('{} {}'.format(test_1.aa,test_1.bb))
# print('{} {}'.format(test_2.aa,test_2.bb))

print(test_1.fullname())
print(test_2.fullname())



