"""Numpy的核心array对象以及创建array的方法"""
"""
    array对象属性：
        array.shape:返回一个元组，表示数组的各次维数组的维数
            对于一维数组，返回的元组形式为(x,)    表示一维数组有x个元素    
            对于二维数组，返回的元组形式为(x,y)   表示二维数组有x个一维数组，每个一维数组有y个元素
            对于三维数组，返回的元组形式为(x,y,z) 表示三维数组有x个二维数组，每个二维数组有y个一维数组，每个一维数组有z个元素
            理解：元组元素个数等于数组的维数，从左至右从高至低地表示次一级维数的数组或元素个数
        
        array.ndim:返回一个整数，表示array的维数
        
        array.size:返回一个整数，表示array中所有元素的个数
            numpy.size(array,0|1)   array数组对象的行数或列数
            
        array.dtype:返回array中元素的数据类型
        
    创建array对象的方法：
        1.python的列表list和嵌套列表创建array:
            array = numpy.array([ ])        一维数组
            array = numpy.array([ [],[], ]) 二维数组
            
        2.使用预定函数：
            numpy.arange([start,] stop[, step,], dtype=None)  创建数字序列（前闭后开，步长）
            
            numpy.ones(shape, dtype=None, order='C')          创建元素全是1的数组 
                                                              shape与array对象属性意义相同，只输入一个整数即指一维数组的元素个数
            
            numpy.ones_like(array, dtype=float, order='C')    创建与array对象形状相同的数组
            
            类似的还有：
                numpy.zeros                                             创建的数组元素全是0
                numpy.zeros_like                                        
                numpy.empty                                             创建的数组元素全是未初始化的随机值
                numpy.empty_like                           
                numpy.full(shape, fill_value, dtype=None, order='C')    创建的数组元素全是指定值fill_value
                numpy.full_like(array, fill_value, dtype=None)                                              
            
        3.random生成随机数的数组

"""
import numpy as np
