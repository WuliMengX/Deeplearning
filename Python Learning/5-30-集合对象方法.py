"""集合对象方法"""
"""对set和frozenset都可用"""
"""     
isdisjoint(other)             #判断是否有交集元素,返回True或False

issubset(other)               #判断集合是否为other的子集,返回True或False,相当于set<=other

issuperset(others)            #判断other是否为集合的子集,返回True或False,相当于set>=other

union(other)                  #返回并集,相当于set | other

intersection(others)          #返回交集,相当于set & other

difference(others)            #返回差集,相当于set - other

symmetric_difference(other)   #返回对称差集,不同时属于两者的元素,相当于set ^ other

"""

"""仅set对象可用"""
"""注:对原数据进行操作"""
"""
set.update(others)                     #更新集合,添加other中的所有元素

set.intersection_update(others)        #更新集合,只保留其中在所有others中也存在的元素

set.difference_update(others)          #更新集合,移除其中也存在于任意一个others中的元素

set.symmetric_difference_update(other) #更新集合,只保留存在于一方而非共同存在的元素

set.add(elem)                          #将元素elem添加到集合中

set.remove(elem)                       #从集合中移除元素elem,不存在引发keyerror

set.discard(elem)                      #从集合中移除元素elem,不存在则无操作

set.pop()                              #从集合中移除并返回任意一个元素,集合为空引发keyerror

set.clear()                            #从集合中移除所有元素

"""