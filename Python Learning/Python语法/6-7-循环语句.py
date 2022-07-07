"""循环语句"""
"""
    while循环
    格式：1.while 判断条件：
              执行语句...
              
          2.while True:    #死循环
              执行语句...
              if 判断条件:  #控制语句
                  break 
                  
          3.while 判断条件:
                执行语句... #如果搭配控制语句，break也会将else停止执行
            else:
                执行语句... #没有控制语句停止执行的话，else的执行语句一定执行
          4.嵌套循环
            while ...:
                ...
                while ...:
                    ...
                 
    for循环
    格式：1.for 变量 in 可迭代对象：   #循环地将可迭代对象内的元素逐一赋值给变量
                执行语句...           #变量可以是多个变量，取决于可迭代对象的数据类型，等价于序列赋值
          
          2.for...in...else
            
          3.嵌套循环
            for 变量 in 可迭代对象：
                执行语句...
                for 变量 in 可迭代对象：
                    执行语句...
                    
    控制语句：break     终止所在的循环语句
             continue  跳过当前，继续到循环位置
"""
"""
    函数：
                range(stop)/range(start,stop,step)  #返回一个按步骤生成的从[start,stop)的整数序列
                                                    #start默认为0
                                                    #range类型相比list和tuple的优势是占用内存小，与表示的范围多大无关

                enumerate(iterable,start=0)         #返回一个enumerate对象（迭代器） 枚举
                                                    #迭代它回得到一个个的元组，每个元组是索引(从start开始，默认0)和索引对应的iterable的值组成的
                                                    
                seasons = ["Spring","Summer","Fall","Winter"]
                object1 = enumerate(seasons)
                print(list(object1))                 #[(0,'Spring'),(1,'Summer'),(2,'Fall'),(3,'Winter')]
                object2 = enumerate(seasons,start=1) #设置开始迭代的索引
                print(list(object2))                 #[(1,'Spring'),(2,'Summer'),(3,'Fall'),(4,'Winter')]
                
                sum(iterable,start=0)     #求和 结果为start+iterable内的数字之和
                
"""














