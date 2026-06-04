import datetime
import time, functools

# --- 装饰器定义区 ---

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args,**kwargs)
        end = time.time()
        total = (end-start)*1000
        print('%s executed in %s ms' % (fn.__name__, total))
        return res
    return wrapper

def log(text = None):
    if callable(text): 
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('begin call')
            result = text(*args, **kw)
            print('end call')
            return result
        return wrapper
    else:
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(f'{text} begin call')
                result = func(*args, **kw)
                print(f'{text} end call')
                return result
            return wrapper
        return decorator

# --- 测试区 ---

print("=== 测试 @log ===")

@log
def f1():
    # 修正了 datetime 的调用方法
    print("当前时间:", datetime.datetime.now())




@log('execute')
def f2(): # 建议换个函数名，避免覆盖上面的 f1
    print("当前时间:", datetime.datetime.now())
    
f1()
print("-" * 20)
f2()

print("\n=== 测试 @metric ===")

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else: 
    print('测试成功!')