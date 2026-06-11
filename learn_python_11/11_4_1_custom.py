class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' %self.name
    
print(Student('Adam'))
s = Student('Jenny')

# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b, self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        a,b = 1,1
        for x in range(n):
            a, b = b, a+b
        return a

# for n in Fib():
#     print(n)
f = Fib()
print(f[0])
print(f[10])