class TestTwo:
    pay_amount = 1.2
    num = 0

    def __init__(self,aa,bb,cc):
        self.aa = aa
        self.bb = bb
        self.cc = cc
        TestTwo.num += 1

    def fullname(self):
        return ('{} {} {}'.format(self.aa,self.bb,self.cc))

    def pay_raise(self):
        self.cc = self.cc * self.pay_amount
    
    
print(TestTwo.num)
emp_1 = TestTwo('join','world',100)
emp_2 = TestTwo('lucy','hello',200)

# print(emp_1.fullname())
emp_1.cc = 1.1
emp_2.cc = 1.2
emp_1.pay_raise()
emp_2.pay_raise()
print(emp_1.cc)
print(emp_2.cc)

print(TestTwo.num)

