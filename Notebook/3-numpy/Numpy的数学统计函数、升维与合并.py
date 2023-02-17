"""Numpy的数学统计函数"""
"""
    以下函数形式都为numpy.函数名()
    都有一个用于指定计算轴为行还是列的参数axis，如果不指定，会计算所有元素的结果
    axis=0 按行的方向计算
    axis=1 按列的方向计算
    
    sum(arr)                     求所有元素的和  返回一个数
    prod(arr)                    求所有元素的积
    cumsum(arr)                  元素的累计和    返回一个数组
    cumprod(arr)                 元素的累计积
    min(arr)                     最小值
    max(arr)                     最大值
    
    percentile(arr,[args])       求数组中0~100百分位数，第二个参数是一个数组，也可以是一个值，返回值的形式与此相同
                                 比如percentile(arr,[25,50,75])返回一个三个元素组成的数组，每个元素分别是arr数组中的25%、50%、75%的分位数（arr数组中有25%、50%、75%的数分别小于这三个元素）
    quantile(arr,[args])         求数组中0~1分位数，与percentile的区别为后面的参数是0~1的小数
    
    median(arr)                  中位数
    mean(arr)                    平均值
    std(arr)                     标准差
    var(arr)                     方差
    average(arr,weights)         加权平均，weights是权重数组，与arr的shape相同
    
    数据标准化：
    标准化一般使用axis=0按行的方向计算列上的数据，也就是每行对应一个样本，每列对应一个样本特征
    
"""

"""numpy中的数组升维"""
"""
    数组可以在数据不变的情况下改变维度
    
    三种方法对一维数组升维：    numpy.newaxis=None 下面可以直接用None代替
    1.    添加一个行维度：
            arr[numpy.newaxis,:]
            numpy.expand_dims(arr,axis=0)
            
    2.    添加一个列维度：
            arr[:,numpy.newaxis]
            numpy.expand_dims(arr,axis=1)
            
    3.    numpy.reshape(arr,shape)方法
"""

"""numpy数组合并操作"""
"""
        numpy.concatenate(arr_list,axis)  arr_list是数组列表，相当于[a,b,c,...]，合并多个数组
                                          axis默认为0，按行合并，即列数不变，行数变，后面的数组依次按行添加到前面的数组下面
                                          axis=1时，按列合并，即行数不变，列数变，后面的数组依次按列添加到前面的数组右边
        
        numpy.stack((arr1,arr2))          按行合并两个一维数组
   
    简单粗暴的合并函数：                                  
        按行合并：
            numpy.vstack(arr_list)
            numpy.row_stack(arr_list)  
        按列合并：
            numpy.hstack(arr_list)
            numpy.column_stack(arr_list)    
        
"""