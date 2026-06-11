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
    # 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，
    # 也可能是一个切片对象slice，所以要做判断
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print(n)
f = Fib()
print(f[0])
print(f[10])
# print(list(range(100))[0:5])
print(f[5:10])
print(f[:10])
# 但是没有对step参数作处理：
print(f[:10:2])

class Student(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
        
s = Student('Adam')
print(s.score)
print(s.age())
# print(s.grade)
class AdvancedChain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return AdvancedChain('%s/%s' % (self._path, path))
    def __call__(self, param):
        return AdvancedChain('%s/%s' % (self._path, param))
    def __str__(self):
        return self._path
    __repr__ = __str__
print(AdvancedChain().user(12345).profile)

class Student(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Adam')
s()

print(callable(Student('Adam')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))