class Student(object):
    __slots__ = ('name','age','score','set_age') # 用tuple定义允许绑定的属性名称
s = Student()
s.name = 'adam'
s.age = 18
# s.score=99 不再slots里面
print(s.name)

def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(25) 新的实例不能用
def set_score(self,score):
    self.score = score
Student.set_score = set_score #给class绑定方法　
s2.set_score(100)
s.set_score(96)
print(s2.score)
print(s.score)

class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 9999
print(g.score)#不管用对继承的子类