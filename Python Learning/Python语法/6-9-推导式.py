"""列表推导式"""
"""
    [x**2 for x in range(3)] #[0,1,4]
    等价于：
    lis = []
    for x in range(3):
        lis.append(x**2)        #[0,1,4]
    
    1.属于表达式
    2.结构由一对方括号里面包含一个表达式，后面跟一个for子句，然后是零个或多个for或if子句组成。
    3.结果将是一个新列表，由表达式一句后面的for和if子句的内容进行求值计算得出
    
    多个for属于嵌套循环
    
    enumerate(iterable,[start=0])   #返回枚举对象，格式为元组(下标,元素)
                                    #>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
                                    #>>> list(enumerate(seasons))
                                    #[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
                                    #>>> list(enumerate(seasons, start=1)) # 下标从 1 开始
                                    #[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
"""

"""字典推导式"""
"""
    {x:y for x,y in enumerate("abcd")}  #{0: 'a', 1: 'b', 2: 'c', 3: 'd'}
    等价于：
    result = {}
    for x,y in enumerate("abcd"):
        result[x] = y
    print(result)
    
"""

"""集合推导式"""
"""
    set = {x**2 for x in range(4)}
    print(set)                      #{0, 1, 4, 9}
"""

"""列表 字典 集合 迭代问题"""
"""
    列表内存自动管理：保证列表元素之间没有间隙
        案例：
                list = [1,2,3]
                
                for item in lis:
                    lis.remove(item)
                    
                print(lis)          #本来是得到一个空列表，但事与愿违 
            
            为什么没有得到一个空列表？
            for循环在遍历序列时是基于索引去获取的，列表[1,2,3]删除元素item = list[0] = 1后，后面的元素因为列表的内存自动管理操作会往前靠
            即会变成[2,3]，接着循环的item = list[1] = 3，列表变成[2]，此时item = list[2]不存在，循环结束。
            
        解决方法：遍历新的，删除老的
                lis1 = [1,2,3,4,5,6]
                lis2 = lis1.copy()      #浅拷贝和深拷贝 lis2 = list(lis1) tuple(lis1) set(lis1) 返回新对象都可以
                for item in lis2:
                    lis1.remove(item)

                print(lis1)
"""
"""字典 集合遍历问题"""
"""
    字典 集合在遍历时，如果改变原数据的size，会造成迭代时报错
        案例：
                dic = {"name": "Tom","age": 18,"height": 188}
                for i in dic:
                    dic.pop(i)
                    print(dic)  #第一次循环：{"age": 18,"height": 188} 第二次报错
                    
                第二次循环时报错，因为原数据的字典size发生改变
                
        解决方法：同上
                dic1 = {"name": "Tom","age": 18,"height": 188}
                dic2 = {"name": "Tom","age": 18,"height": 188}
                for i in dic2:  #不能用dic1.keys() 返回一个视图 会随原数据改变
                    dic1.pop(i)
                    print(dic1)
                
"""
