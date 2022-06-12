"""字典对象方法"""
"""
目标为返回值的方法：        
    1.dict.keys()           #键
    2.dict.values()         #值
    3.dict.items()          #对  
    4.dict.get(key,default) #指定键的值
    5.dict.copy()

目标为操作原字典的方法：
    1.dict.update(other)    #添加更新覆盖
    2.dict.clear()

既有返回值，又对原字典操作的方法：
    1.dict.setdefault(key,default) #存在key就返回对应值，不存在就加入key=default并返回default
    2.dict.pop(key,default)        #移除指定键，返回对应值或default或报错
    3.dict.popitem()               #移除最后一个键值对，返回剩余字典元素构成的元组
"""

"""
dict.keys()           #返回由字典的键组成的一个新视图，视图与原数据有关联
                      #返回的对象是视图对象，当字典改变时，视图也会相应改变

dict.values()         #返回由字典的值组成的一个新视图
                      #与keys类似

dict.items()          #返回由字典的键值对组成的一个新视图

dict.get(key,default) #返回指定的键key对应的值，若key不在字典中，返回default
                      #key为指定的键，若指定的键不存在就返回default，默认为none
                      
dict.update(other)    #使用来自other的键/值对更新字典，如果键相同，则覆盖原有的键
                      #other：可以是另一个字典对象；一个包含键/值对的可迭代对象；或(关键字=参数)这样的形式

dict.pop(key,default) #移除指定的键key，并返回对应的值，如果key不在字典中，返回default
                      #如果default未给出且key不存在字典中，则会引发报错
                      
dict.popitem()        #从字典中移除最后一个键值对，并返回它们构成的元组（键，值）        
                          
dict.setdefault(key,default)    #如果字典存在键key，返回它的值
                                #如果不存在，加入值为default的键key，并返回default，默认为none

dict.copy()           #返回原字典的浅拷贝

dict.clear()          #移除字典中所有元素，无返回值  

map(key,iterable)     #将函数key作用到可迭代对象中的每一个元素，返回一个迭代器
"""
