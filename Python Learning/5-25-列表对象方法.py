"""列表对象方法"""
"""
修改列表使用索引和切片的方式：
    1.索引修改单个元素
    2.切片修改多个元素

有返回值的列表对象方法：
    1.list()
    2.sorted()
    3.reversed()
    4.list.count()
    5.list.index()
    6.list.pop()
    7.list.copy()

对原数据操作的方法：
    1.list.append()
    2.list.extend()
    3.list.insert()
    4.list.sort()
    5.list.reverse()
    6.list.pop()
    7.list.remove()
    8.list.clear()

list(iterable)        #将可迭代对象转化为列表并返回，无参数返回空列表
                      #字典只取键值
                      #对象为字符串时每个字符都会转化为列表的一个元素

list.append(x)        #列表末尾添加一个元素，可以是可迭代对象，但会将其整体作为一个元素添加至末尾
                      #修改原列表，无返回值

list.extend(iterable) #将可迭代对象中的所有元素扩展至原列表，
                      ##修改原列表，无返回值
                      #与append不同点在于可迭代对象的每个元素都作为单独一个元素添加至末尾

list.insert(i,x)      #给定位置插入一个元素
                      #修改原列表，无返回值    

list.sort(key=,reverse=False)           #对原列表排序，无返回值
                                        #key为指定函数，排序之前会先应用函数之后再排序
                                        #False和True指定升序和降序             

sorted(iterable,key=,reverse=False)     #对可迭代对象排序，不对原数据操作
                                        #对任何对象都以列表形式返回
                                        #与sort相比，对任何可迭代对象都可使用，有返回值，内置函数

list.reverse()          #对列表中的元素反向，无返回值
                        #只针对列表，对原数据操作
 
reversed(seq)           #对给定序列返回一个反向迭代器    
                        #只针对序列，不对原数据操作，内置函数
 
list.count(x)           #返回元素x在列表中出现的次数

list.index(x,start,end) #返回从列表中第一次找到x的位置索引，找不到报错
                        #返回的索引是对于整个序列的索引
                    
list.pop(i)             #删除列表中给定位置的元素并返回该元素
                        #修改原列表
                        #如果没有给定位置，会对最后一个元素操作（栈操作）

list.remove(x)          #移除列表中第一个值为x的元素
                        #修改原列表，无返回值
                        #如果找不到就报错

list.copy()             #返回列表的一个浅拷贝
                        #等价于list[:]

list.clear()            #移除列表所有元素
                        #修改原列表，无返回值
                        #等价于del list[:]
"""

"""零散知识点"""
"""
1.切片后不会降维，比如列表的切片依然为列表
2.除了数字外的其他类型都是可迭代对象
3.切片赋值时，Python不支持单个值赋值
"""