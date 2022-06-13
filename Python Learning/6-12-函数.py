"""自定义函数"""
"""
    格式：def name(参数):
            函数体
            
        1.函数调用：形参-函数中声明的参数 实参-调用时传入的参数
        2.return    #后面可跟单个对象 多个对象 表达式 不跟，多个对象会以元组的形式返回
                    #把后面跟的值返回给调用方 结束对应函数
        3.文档注释  函数名(): 底下注释 存放在.__doc__
        4.内置函数：与数学相关的
            help()  #内置帮助系统 交互式
            
            abs(x)  #x可以是整数 浮点数 布尔型 复数 返回绝对值或者模
            
            divmod(a,b)  #a,b皆为数字非复数 返回一个包含商和余数的元组
            
            max(iterable,*[,key,default])   #返回给定参数的最大值   字符串比大小只比字符串的第一位的值
            max(arg1,arg2,*args[,key])      #iterable为空时，返回default指定的值，不指定则报错,key指定函数
        
            min(iterable,*[,key,default])   #返回给定参数的最小值
            min(arg1,arg2,*args[,key])
            
            pow(base,exp[,mod])             #返回base的exp次幂；若mod存在，返回base的exp次幂对mod取余
            
            round(number[,ndigits])         #返回number四舍五入到小数点后ndigits位精度的值 
                                            #ndigits如果省略或为None，则返回值为整数，否则返回值和number类型相同
                                            #精确到整数位，距离两个不同的数相同，则选择其中的偶数
                                            
            sum(iterable,/,start=0)         #元素必须为数字类型的可迭代对象，start为累加的起始数字，默认为0
                                            #从start开始自左向右对iterable的项求和并返回                         
                                            
                                            
"""
