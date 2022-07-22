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
    def __init__(self,f):   # f:washer
        self.func = f
        
    def __call__(self):
        start = time.time()
        self.func()
        end = time.time()
        print(f"衣服洗好了，总共花费{end-start}秒，快来拿吧~")

@Timer
def washer():   #相当于 obj = Timer(washer) 实例化
    time.sleep(2)
    print("滴滴滴滴滴......")
    
washer()        #obj()  实例对象像函数一样调用时会自动调用__call__


"""带参数的类装饰器"""
class Interaction:
    def __init__(self, name):
        self.name = name
    def __call__(self, func):
        def deco(work_time):
            print(f"{self.name}, 你好, 请把要洗的衣物放进来!")
            func(work_time)
            print(f"{self.name}, 我帮你把衣物洗好了, 快来拿!")
        return deco

@Interaction("张三")
def washer(work_time):
    time.sleep(work_time)
    print("嘀嘀嘀...")
    
"""
执行顺序说明：
    代码从上往下执行, 先导入time模块, 定义Interaction类和方法, 执行到@Interaction装饰器时,
    该类装饰器进行实例化, 调用初始化方法, 创建实例变量, __new__返回实例对象, 再定义washer函数,
    当被装饰的函数定义好了, 则将被装饰的函数作为参数调用实例对象, 即Interaction("张三")(washer),
    即调用__call__方法, 定义deco函数并返回其引用, 所以当最后执行washer(3)时, 其实等价于deco(3), 而其中又调用了func函数, 即washer函数 
"""
washer(3)


"""多个装饰器"""
def deco(func):
    def wrapper1(*args):
        res = func(*args)
        return res
    return wrapper1

def timer(func):
    def wrapper2(*args):
        star_time = time.time()
        res = func(*args)
        end_time = time.time()
        print("函数耗时:{}".format(end_time-star_time))
        return res
    return wrapper2

"""
timer(add) --> wrapper2 
deco(wrapper2) --> wrapper1
add = wrapper1
add(3,4,5) --> wrapper1(3,4,5)

多个装饰器，从下往上调用，后进先出
"""
@deco
@timer
def add(*args):     
    time.sleep(2)
    return sum(args)

"""
执行顺序说明：(执行顺序参考堆栈)
    代码从上往下执行, 先导入time模块, 定义deco函数和timer函数, 执行到@deco和@timer,
    这两个装饰器都没有调用, 再定义add函数, 当被装饰的函数定义好了,则将被装饰的函数作
    为参数传入装饰器函数并执行, 即timer(add), 定义wrapper2并返回其引用, 然后把返回的
    wrapper2作为参数传入装饰器函数并执行, 即deco(wrapper2), 定义wrapper1并返回其引用,
    所以最后add(3, 4, 5)时, 其实等价于wrapper1(3, 4, 5), 而执行wrapper1(3, 4, 5)时,
    其中的func即deco的参数func, 即wrapper2, 所以又会调用wrapper2函数, 而wrapper2函数
    中的func即timer的参数func, 即add, 所以再调用add得到结果,wrapper2函数中返回的res,
    再给wrapper1中的res再最后返回 
"""
print(add(3, 4, 5))


"""内置装饰器"""
"""
    @classmethod
        将类中的方法装饰为类方法
    
    @staticmethod
        将类中的方法装饰为静态方法
        
    @property
        将类中的方法装饰为只读属性，调用方法名即可得返回值
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def adult_age_p(self):
        return 18

    def adult_age(self):
        return 18

    @property
    def adult_flag(self):
        return self.age >= self.adult_age_p

stu = Student("张三", 18)
print(stu.adult_age())      # 没有加@property, 必须使用正常的调用方法的形式, 在后面加()
print(stu.adult_age_p)      # 加了@property, 用调用属性的形式来调用方法, 后面不需要加()
print(stu.adult_flag)       # True
stu.age = 17                # 可以修改stu对象的age属性
                            # stu.adult_age_p = 19 # 报错：@property将方法装饰为只读属性, 不能修改
print(stu.adult_flag)       # False