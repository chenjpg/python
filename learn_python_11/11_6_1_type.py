from hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
def fn(self,name='world'):
    print('Hello,%s.'%name)
Hello1 = type('Hello1',(object,),dict(hello=fn))# 创建Hello class
h1 = Hello1()
h1.hello()
print(type(Hello1))
print(type(h1))
# 要创建一个class对象，type()函数依次传入3个参数：

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
class ListMetaclass(type):
    def __new__ (cls, name ,bases,attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls,name,bases,attrs)

class MyList(list,metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print(L)
L2 = list()
# 而普通的list没有add()方法：
# L2.add(1)

class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' %(self.__class__.__name__,self.name)
    
class StringField(Field):
    def __init__(self, name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField,self).__init__(name,'bight')

class ModeMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s' %name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s' % (k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls,name,bases,attrs)
    

class Model(dict,metaclass=ModeMetaclass):
    def __init__(self, **kw):
        super(Model,self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Model' object hase no attribute '%s'" %key)
    def __setattr__(self,key,value):
        self[key]= value
    
    def save(self):
        field=[]
        params=[]
        args=[]
        for k,v in self.__mappings__.items():
            field.append(v.name)
            params.append('?')
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) value (%s)'%(self.__table__,','.join(field),','.join(params))
        print('SQL: %s'%sql)
        print('ARGS: %s'%str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345,name='adam',email='test@orm.org',password='mypwd')
u.save()


