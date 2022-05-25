"""字符串对象方法"""
"""
str.replace(old,new,count)    #将字符串中old字符串替换为new字符串 count默认-1 替换所有能替换的

str.strip(chars) #chars指定要移除的字符序列 默认移除空白符
                 #从字符串左右两边删除指定的字符序列 会考虑chars的所有组合

str.center(width,fillchar)               #与下类似 返回的字符串中原字符串在其正中
str.ljust(width,fillchar) ; str.rjust()  #width指定返回的字符串长度
                                         #fillchar填充字符 必须是单个字符 默认空格符
                                         #返回长度为width的字符串 原字符串靠左对齐 使用fillchar填充空位

str.partition(sep) ; str.rpartition()  #sep分隔符
                                       #在sep首次出现的位置拆分字符串 返回一个包含三个元素的元组 （"分隔符之前的部分","分隔符本身","分隔符之后的部分"）
                                       #未找到分隔符 返回的元组包含字符串本身以及两个空字符串

str.startswith(prefix,start,end) ; str.endswith()             #prefix匹配前缀 可以是字符、字符串、或者元组（元组中只要一个元素满足即可）
                                                              #判断字符串是否以指定的prefix开始 返回true或false

str.isalnum() ; str.isalpha() ; str.isdigit() ; str.isspace() #判断字符串所有字符是否都为字母、文字或数字
                                                              #字母、数字、空白符
                                                              #返回true或false

str.split(sep=None,maxsplit=-1) ; str.rsplit()                #sep是分割字符串的分隔符 默认为所有空白符
                                                              #maxsplit最大分割次数 默认-1 分隔所有
                                                              #指定分隔符对字符串进行分割 返回字符串列表 返回结果不包括分隔符

str.join(iterable) #iterable包括字符串、列表[,]、元组(,)、字典{:}、 集合{,} 返回字符串
                   #用str（指定字符）连接iterable对象中的元素（必须是字符串类型）
                   #字典只取键，不取值 
                   #集合无序，所以返回结果不确定

str.count(sub,start,end)                 #返回子字符串在字符串中出现的次数 默认全局搜索

str.find(sub,start,end) ; str.rfind()    #从左第一次找到子字符串时的索引，找不到返回-1，start和end可不填
str.index(sub,start,end) ; str.rindex()  #从右
                                         #index与find类似 但index找不到就会报错 其他一样

str.capitalize() #首字母变大写 其他变小写 返回字符串
str.title()      #所有单词首字母变大写 其他变小写 
str.upper()      #所有字符变大写 
str.lower()      #所有字符变小写 
str.swapcase()   #所有字符大写变小写 小写变大写

"""

"""零散知识点"""
"""
1.切片后不会降维，比如列表的切片依然为列表
2.除了数字外的其他类型都是可迭代对象
3.切片赋值时，Python不支持单个值赋值
"""

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
                      #与apeend不同点在于可迭代对象的每个元素都作为单独一个元素添加至末尾

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