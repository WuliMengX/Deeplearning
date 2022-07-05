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









