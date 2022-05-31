"""赋值"""
"""知识点"""
"""
    1.变量定义和赋值必须同时进行
    2.id(object):唯一标识符,返回值的内存地址,而不是变量的
    3.[-5,256]之间的数字使用的都是同一个对象同一个地址
    4.小整数对象池:一个值可以被多个变量名引用,变量值的引用计数为0时认定为不可用,会回收内存空间
    5.可变数据类型的数据被多个变量引用时,原数据被修改,所有引用都会改变
"""

"""浅拷贝"""
"""知识点"""
"""
    "可变就复制,不可变就赋值"
    
    copy.copy()     浅拷贝
    1.如果浅拷贝对象是不可变数据类型,那么和赋值语句等效(无拷贝意义)
    2.如果浅拷贝对象是可变数据类型,浅拷贝会将该对象复制一份,但该对象中的其他所有元素仍为引用关系
    
    copy.deepcopy() 深拷贝 
    1.如果深拷贝对象是不可变数据类型,复合类型还需要所有元素都不可变,那么和赋值语句等效(无拷贝意义)
    2.如果深拷贝对象是可变数据类型,深拷贝会将该对象复制一份,对于其中的元素分别递归地去适用前两点规则
"""
import copy

tup1 = (991,"abc")
tup2 = copy.copy(tup1)
print(id(tup1))
print(id(tup2))

tup3 = (991,"abc",[])
tup4 = copy.copy(tup3)
print(id(tup3))
print(id(tup4))

tup5 = [991,"abc"]
tup6 = copy.copy(tup5)
print(id(tup5))
print(id(tup6))