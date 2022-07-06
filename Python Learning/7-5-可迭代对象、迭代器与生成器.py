"""可迭代对象与迭代器"""
"""
    除了数字型以外的其他基本数据类型都是可迭代对象
    range对象是可迭代对象
    
    zip map filter enumerate reversed对象是迭代器
    文件对象也是迭代器：
        with open("文件路径",mode="r") as file:
            print(isinstance(file,Iterable))      
        
    可迭代对象(Iterable)、迭代器(Iterator)都是Iterable的子类
    
    迭代器一定是可迭代对象，生成器(Generator)一定是迭代器，反之则不对
"""

"""可迭代对象"""
"""
    满足其一条件即可：
        1.支持 迭代 协议（有__iter__()方法）
        2.支持 序列 协议（有__getitem__()方法，且数字参数从0开始）
    
    判断是否为可迭代对象(返回True或False)：
    "__iter__" in dir(对象名) or "__getitem__" in dir(对象名)
    
    dir()函数：   
        不带参数时，返回当前范围内的变量、方法和定义的类型列表
        带参数时，返回参数的属性、方法列表
        如果参数包含方法__dir__()，该方法将被调用。
        如果参数不包含__dir__()，该方法将最大限度地收集参数信息
        
    自定义可迭代对象：
        只要支持迭代协议或者序列协议即可
        方式（满足其一即可）：
            1.类里定义 def __iter__(self)
            2.类里定义 def __getitem__(self,index)
    
    注意：isinstance(对象,Iterable)可以检测对象是否有__iter__()方法，但无法检测是否能够使用__getitem__()方法进行迭代
         当对象只支持序列协议时，对象只有__getitem()方法，属于可迭代对象，但是不能用isinstance判断是否为可迭代对象
           
"""

"""迭代器"""
"""
    支持 迭代器 协议（注意区分迭代协议），即同时满足两个条件：
        1.实现__iter__()方法
        2.实现__next__()方法
    迭代器协议包含迭代协议
    
    判断是否为迭代器：
    1."__iter__" in dir(对象名) and "__next__" in dir(对象名)
    2.isinstance(对象名,Iterator)
    
    自定义迭代器：
        只要支持迭代器协议即可
        方式：
            类里同时定义 def __iter__(self)
                        def __next__(self)
                        
"""

"""迭代的逻辑"""
""" 
    __iter__是魔术方法，在迭代时会被自动调用：
        1.以for循环为例，循环遍历时会自动调用__iter__魔术方法
        2.__iter__必须返回迭代器对象，因为每次循环时会用该迭代器对象自动调用__next__(既是魔术方法又是对象方法，只能由实例对象调用)
        3.把每次调用__next__的返回值赋值给变量i
        
    可迭代对象迭代时：先找__iter__方法，没有的话再找__getitem__方法
        如果有__iter__方法(可能是迭代器或非迭代器)：
                1.可迭代对象里的__iter__返回一个迭代器，通过迭代器里的__next__实现迭代
                2.迭代器里的__iter__返回它本身（迭代器也是可迭代对象，它的__iter__方法返回本身这个迭代器即可）
                3.迭代器里的__next__()方法返回可迭代对象的下一项，如果没有下一项可返回，则抛出StopIteration异常
                
            __iter__只在迭代初调用一次，后面调用的都是__next__
            根据迭代的逻辑，可迭代对象迭代时，调用__iter__返回的迭代器对象不是本身，所以迭代完后可以继续实现迭代
                
        如果只有__getitem__方法：
                找到__getitem__(self,index)方法，然后每一次迭代都会调用一次__getitem__方法
                其中index参数从0开始，自动无限递增+1
                当index超出iterable索引范围抛出IndexError异常，停止迭代                
                
"""

class ListIterator:
    def __init__(self,obj):         # obj为MyList类的实例对象
        self.obj = obj
        self.count = 0              # 从这里可以知道，代过的迭代器无法马上再次迭代
                                    # 因为再次使用时，self.count不为0，所以需要再次实例化迭代对象才能使用
    def __iter__(self):
        return self
    
    def __next__(self):     #魔术方法 对象方法
        if self.count < len(self.obj.iterable):
            item = self.obj.iterable[self.count]
            self.count += 1
            return item
        raise StopIteration

class MyList:
    
    def __init__(self,iterable):
        *self.iterable, = iterable
        
    def __repr__(self):
        return f"{self.iterable}" 
    
    # def __iter__(self):
    #     return ListIterator(self)   # self为MyList类的实例对象，作为迭代器的形参传入
    
    def __getitem__(self,index):      # index会自动递增
        return self.iterable[index]
    
# for i in ListIterator(MyList(1,2,3)): # for循环能接收StopIteration异常停止循环
#     print(i)

# mylis = MyList((1,2,3))

# for i in mylis:
#     print(i)
    
# lis_iter = mylis.__iter__()     # 上面for循环的原理
# while True:
#     try:
#         i = lis_iter.__next__()
#         print(i)
#     except StopIteration:
#         break

# mylis = MyList(('a','b','c','d'))
# print(mylis)
# for i in mylis:
#     print(i)

"""生成器"""
"""
    生成器写法类似于标准的函数写法，不同点在于：
        生成器用 yield 语句返回数据，而标准的函数用 return 语句返回数据
        yield 语句返回数据之后会挂起函数的状态，并会记住上次执行语句时的所有数据值
        方便每次在生成器调用__next__()方法时，从上次挂起的位置恢复继续执行
        而return 语句返回一次数据之后，函数就结束了
        
    生成器(Generator)是迭代器，满足迭代器协议，同时有__iter__和__next__方法
    调用__next__方法时，会执行函数体，直到运行到一个yield语句时结束，此时yield等同于return
    多次调用__next__方法时，会继续执行函数体到下一个yield语句，直到没有yield语句抛出StopIteration异常
    
    对生成器迭代时，生成器就是迭代器，区别是生成器是函数，迭代时也会执行函数体
    注意对同一个生成器，迭代过以此后不能马上再次迭代，原理与迭代器相同
    
    函数中只要有yield语句就一定是生成器函数
    此时，函数中的yield语句后面的return返回值会返回给StopIteration异常，停止执行
    
"""
# from typing import Generator,Iterable

# def func1():
#     print(1)
#     return "a"
#     print(2)
#     return "b"
#     print(3)
#     return "c"
#     print("ending")
    
# # res1 = func1()
# # print(res1)

# def func2():                        # 生成器函数
#     print(1)
#     yield "a"
#     print(2)
#     yield "b"
#     print(3)
#     yield "c"
#     print("ending")
    
# res2 = func2()                      # <generator object func2 at 0x000001C7A43E2730>
# print(res2)
# print(isinstance(res2,Generator))   # True
# print(isinstance(res2,Iterable))    # True
# print("__iter__" in dir(res2) and "__next__" in dir(res2))  # True

# print(res2.__next__()) 
# print(res2.__next__())   
# print(res2.__next__())   
# print(res2.__next__())   
# print(res2.__next__())   # 抛出StopIteration异常
                 
# for i in res2:           # 不注释上面的代码的话，此处不运行
#     print(i)

# def gen():
#     print("starting")
#     print(res1 := (1,2))
#     res2 = yield 4,5
#     print(res2)
#     res3 = yield res1
#     print(res3)
#     print(res1)
    
# g = gen()
# print(g.__next__())     # 执行函数体到第4行挂起函数状态，终端输出：starting (1, 2) (4, 5)
# print(g.__next__())     # None (1,2)
# print(g.__next__())     # None (1,2)


"""生成器表达式"""
"""

"""