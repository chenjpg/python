
print(type(123),type('srt'),type(None),type(abs))
print(type(123)==type(456),
type(123)==int,
type('abc')==type('123'),
type('abc')==str,
type('abc')==type(123),)

import types
def fn():
    pass
print(type(fn)==types.FunctionType,type(abs)==types.BuiltinFunctionType,type(lambda x: x)==types.LambdaType,type((x for x in range(10)))==types.GeneratorType)

class animal(object):
    def run(self):
        print('animal can run')
class dog(animal):
    def run(self):
        print('dog running')
    
class husky(dog):
    def run(self):
        print('Husky is running')
a = animal()
d = dog()
h = husky()
print(
isinstance(h, husky),
isinstance(h,dog),
isinstance(h,animal),
isinstance(h,husky) and isinstance(d,animal),
isinstance(d,husky),
isinstance('a', str),
isinstance(123,int),
isinstance(b'a',bytes),
isinstance([1,2,3],list),
isinstance((1,2,3),tuple)
)

# print(dir('abc'))
print(len('abc'))
print('abc'.__len__())
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))
print('ABC'.lower)
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(hasattr(obj,'x'),
      obj.x,
      hasattr(obj,'y'),
      setattr(obj,'y',19),
      hasattr(obj,'y'),
      getattr(obj,'y'),
      obj.y)
print(getattr(obj,'z',404),
      hasattr(obj,'power'),
      getattr(obj,'power'))
fn = getattr(obj,'power')
print(fn())