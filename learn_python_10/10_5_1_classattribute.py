class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'bob'
print(s.name)
print(Student.name)
del s.name
print(s.name)

