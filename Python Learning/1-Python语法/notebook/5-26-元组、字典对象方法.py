"""元组对象方法"""
"""
零碎知识点：
    1.元组和列表类似，都是序列，[]变成了()，但元组是不可变的
    2.元组不可变，但元组中的列表可变
    3.多个值赋给一个变量时，python会自动将这些值封装为一个元组
    4.元组的对象方法与列表类似，但只有不改变元素的对象方法
"""
"""
tuple(iterable) 

tuple.count(x)  

tuple.index(x,start,end)

"""

"""字典对象方法"""
"""
零碎知识点：
    1.字典可变，不是序列
    2.冒号(:)分割，逗号(,)分隔，包括在花括号({})中
    3.键和键包含的内容必须为不可变类型（数字、字符串或元组）
    4.键重复会覆盖，后面覆盖前面，但是位置不变
    5.值的数据类型没有严格限制，可以重复

创建字典的六种方法：
    1.空字典{}里写键值对
    dic = {'键':值,}

    2.定义空字典，再往里面添加键值对
    dic = {}
    dic['键'] = 值

    3.把键作为关键字传入
    dic = dict( 键 = 值, )

    4.可迭代对象方式构造字典
    dic = dict( [ ("键",值) , ] ) #这里用元组

    5.通过zip()把对应元素打包成元组，类似上一种方法
    dic = dict(zip( ["键",], [值,] ) )

    6.利用类方法fromkeys()创建
    dic = dict.fromkeys( ("键", ) )      #所有键都为None
    dic = dict.fromkeys( ("键",), "值")  #所有键的值都为"值"
    示例： 
    dic1 = dict.fromkeys(("name", "age", "sex"))
    print(dic1)
    dic2 = dict.fromkeys(("name", "age", "sex"), "I don't know!")
    print(dic2)
"""
"""
zip(iterable) #返回一个元组的迭代器，其中第i个元组包含来自每个参数序列或可迭代对象的第i个元素
              #当所输入可迭代对象中最短的一个被耗尽时，迭代器停止迭代
              #不带参数返回空迭代器
              #当只有一个可迭代对象参数时，返回一个单元组的迭代器

dict(**kwarg/mapping/iterable)           #创建一个字典并返回
        1.dict( 键=值 , )                传入关键字来构造字典
        2.dict( zip(["键",],[值,]) )     映射函数方式构造字典
        3.dict( [("键",值), ] )          迭代对象方式构造字典

"""
