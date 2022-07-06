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
        
    可迭代对象(可以是迭代器或非迭代器)迭代时：先找__iter__方法，没有的话再找__getitem__方法
        如果有__iter__方法：
                1.可迭代对象里的__iter__返回一个迭代器，通过迭代器里的__next__实现迭代
                2.迭代器里的__iter__返回它本身（迭代器也是可迭代对象，它的__iter__方法返回本身这个迭代器即可）
                3.迭代器里的__next__()方法返回可迭代对象的下一项，如果没有下一项可返回，则抛出StopIteration异常
                
                (__iter__只在迭代初调用一次，后面调用的都是__next__)
                
        如果只有__getitem__方法：

                
                
                
                
                
                
"""
class ListIterator:
    def __init__(self,obj):         # obj为MyList类的实例对象
        self.obj = obj
        self.count = 0
        
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
    
    def __iter__(self):
        return ListIterator(self)   # self为MyList类的实例对象，作为迭代器的形参传入
    
# for i in ListIterator(MyList(1,2,3)):
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





