class Student(object):
    name = 'Student'#这样是类属性
# class Student(object):
#     def __init__(self, name):
#         self.name = name
# 必须先创建对象（实例化）才能访问。每创建一个新对象，内存中就会开辟一块新空间来存放这个对象的 name。
s = Student()
print(s.name)
print(Student.name)
s.name = 'bob'
print(s.name)
print(Student.name)
del s.name
print(s.name)

