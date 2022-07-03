"""装饰器"""
"""
    装饰器，顾名思义就是起装饰作用的，不改变原来函数作用的，只是在原来函数上增加些额外的功能
    
    装饰器并不是编码必须性，不使用装饰器也完全可以，很多时候使用它是为了：
        使代码更加优雅，结构更加清晰
        将实现特定的功能代码封装成装饰器，提高代码复用率，增强代码可读性

"""
"""不带参数的函数装饰器"""
import time
from tracemalloc import start
def timer(func):  # 闭包函数
    def wrapper(sleep_time):
        t1 = time.time()
        func(sleep_time)
        t2 = time.time()
        cost_time = t2 - t1
        print(f"花费时间：{cost_time}秒")
    return wrapper


@timer  # 装饰器 当被装饰的函数(func)定义好时，会把它作为参数传给装饰器函数并调用，即timer(func)
def func(sleep_time):  # 然后执行timer函数，定义wrapper，再返回wrapper，最后执行func2(2)，其实就是执行wrapper(2)
    time.sleep(sleep_time)
    print("执行func函数了~")


# func = timer(func)            装饰器的作用就相当于这一行代码
func(2)  # 相当于 wrapper = timer(func)
#       wrapper(2)

"""执行顺序说明"""
"""
    代码从上往下执行, 先导入time模块, 定义timer函数, 再执行到@timer装饰器
    该函数装饰器没有调用, 再定义function函数, 当被装饰的函数定义好了
    则将被装饰的函数作为参数传入装饰器函数并执行, 即timer(function), 返回wrapper函数的引用
    所以当最后执行function(3)时, 其实等价于wrapper(3), 而wrapper函数中又调用了func函数,即function函数 
"""


"""带参数的函数装饰器"""
def interaction(name):
    def timer(f):
        def wrapper(sleep_time):
            start = time.time()
            f(sleep_time)
            end = time.time()
            print(f"{name},洗衣机花费时间：{end - start}")
        return wrapper
    return timer

@interaction("翠花")        #返回 timer
def washer(sleep_time):     #当被装饰的函数定义好时，会把它作为参数传给装饰器执行后返回的函数并调用，即timer(washer)
    time.sleep(sleep_time)  #然后定义wrapper并返回
    print("嘀嘀嘀......")


washer(3)                   #即wrapper(3)

"""不带参数的类装饰器"""
class Timer:
    def __init__(self,f):
        start = time.time()
        f()
        end = time.time()
        print(f"衣服洗好了，总共花费{end-start}秒，快来拿吧~")

@Timer
def washer():   #相当于 obj = Timer(washer) 实例化
    time.sleep(2)
    print("滴滴滴滴滴......")
    
washer()        #obj()


