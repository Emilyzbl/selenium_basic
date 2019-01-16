import datetime

class TestTwo:
    pay_amount = 1.2
    num = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + last + '@123.com'
        self.pay = pay
        TestTwo.num += 1

    def fullname(self):
        return ('{} {} {}'.format(self.first, self.last, self.pay))

    def pay_raise(self):
        self.pay = self.pay * self.pay_amount
    

    @classmethod
    def set_raise_amount(cls,amount):
        cls.pay_amount = amount

    @classmethod
    def from_str(cls,str):
        (first,last,pay) = str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        else :
            return True


nowday = datetime.datetime(2018,4,12)
# print(TestTwo.is_workday(nowday))


emp_1 = TestTwo('join','world',100)
emp_2 = TestTwo('lucy','hello',200)

TestTwo.set_raise_amount(1.5)

emp1_str = 'join-hello-100'
emp2_str = 'lily-good-200'

# (first,last,pay) = emp1_str.split('-')
# new_emp1 = TestTwo(first,last,pay)

new_emp1 = TestTwo.from_str(emp1_str)
new_emp2 = TestTwo.from_str(emp2_str)
# print(new_emp1.fullname())
# print(new_emp2.fullname())

(aa, bb, cc) = emp1_str.split('-')
print('{} {} {}'.format(aa, bb, cc))

