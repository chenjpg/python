import time
def timing_decorator(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args, *kwargs)
        end_time = time.time()
        print(f"function {func.__name__}took[{end_time - start_time:.6f} seconds to execute")
        return result 
    return wrapper


@timing_decorator
def example_function(n):
    sum=-0
    for i in range(n):
        sum += i
    return sum


result = example_function(10000)