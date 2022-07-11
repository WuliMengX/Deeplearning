"""Numpy对数组的索引查询"""
"""
    三种索引方法：
        基础索引
        神奇索引
        布尔索引
        
    主要针对一维数组和二维数组：
    
        基础索引：
            一维数组：array[index]          与python的list一样，返回下标为index的值
                     array[start:end]      切片，start和end都可省略，左闭右开
                     
            二维数组：Array[x,y]    #Array[x][y]      索引单个值，x,y分别为行坐标和列坐标，实现行列筛选，返回x行y列的值
                     Array[x]      #Array[x,:]       索引行和列，省略代表筛选所有，返回的数据实际上是降低一个维度的数组
                     
                    先看","号再看":"号，","号前的":"号是对行筛选，","后的":"号是对列筛选
                    ","号后的数字是开区间的，不包含在内，","前后单个值代表只筛选指定下标的行或列
                    举例，X[:2,2:4]代表对二维数组从0行筛选到1行，从2列筛选到3列
                    X[:,2]代表对二维数组筛选所有行，再筛选2列
            注意：切片的修改会修改原来的数组，原因是Numpy经常处理大数据，避免每次都复制
            
        神奇索引：了解即可
            一维数组：X = array[[x,y,z]]    取array数组中下标为x,y,z的元素 X = [array[x],array[y],array[z]]
                    
                     indexs=[[a,b],[c,d]] 
                     X = array[indexs] = [[x,y],        X = [[array[a],array[b]],               
                                          [m,n]]             [array[c],array[d]]]
            实例：获取数组中最大的前N个数组
              # 随机生成1到100之间的，10个数字
                arr = np.random.randint(1,100,10)
                arr # [18, 79, 33, 20, 30, 69, 37, 16, 34, 85]
                
              # arr.argsort()会返回排序后的索引index
              # 取最大值对应的3个下标，返回的是index
                arr.argsort()[-4:] # [6, 5, 1, 9]
              
                arr[arr.argsort()[-4:]] # [37, 69, 79, 85]
              
            二维数组：
                Array[[x,y]]       筛选多行，列可以省略，相当于Array[[0,2],:]取0行和2行所有的列
                Array[:,[x,y,z]]   筛选多列，行不可以省略，取x列，y列和z列
                Array[[x,y],[m,n]] 同时筛选行列，取x,y行的m,n列，返回一维数组
              
        布尔索引：用的最多
            一维数组：array>5   返回一个一维数组，数据类型为布尔值，只有True和False，原来的数组array不变
                               如果array内的元素大于5，则该一维数组同样下标的布尔值为True，否则为False
                               
                     array[array>5] 返回一个一维数组，依次为array数组内大于5的元素
            实例：把一维数组进行0 1化处理
            比如把房价数字，变成“高房价”为1，“低房价”为0
                x[x<=5] = 0     #执行x<=5时相当于将x数组内的值依次与5比较，逐个返回True或False，x[True]时将该位置的元素赋值为0，x[False]时不变
                x[x>5] = 1
                x   # [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
                
                x = np.arange(10)
                x[x < 5] += 20
                x   # [20, 21, 22, 23, 24,  5,  6,  7,  8,  9]
            
            二维数组：Array>5           返回一个二维数组，与一维数组的情况相同
                     Array[Array>5]    返回的依然时一个一维数组      
            实例：怎样把第3列大于5的行筛选出来
                X[:, 2]           返回数组所有行的第3列的值组成的一维数组
                X[:,2]>5          返回值参照一维数组的布尔索引
                X[X[:,2]>5]       返回按行筛选出的第3列大于5的行组成的二维数组
                X[X[:,2]>5] = 666 修改原数组，第3列大于5的行的元素都被修改成666
                
        条件组合
        实例：
            x = np.arange(10)
            condition = (x%2==0) | (x>7)    注意每个条件都要加括号
                                            与一维数组布尔索引类似，满足条件为True，否则为False
            x[condition]                    返回一维数组，元素为满足条件的原数组的值
              
"""
import numpy as np

X = np.arange(10)
print(X>5)
