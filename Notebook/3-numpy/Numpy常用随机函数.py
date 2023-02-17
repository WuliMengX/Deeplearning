"""numpy常用随机函数"""
"""
    全都是属于numpy.random模块的函数，使用方法都是 numpy.random.函数名()
    
    rand(shape)                       返回的随机数值在[0,1)
    
    randn(shape)                      返回的随机数值具有标准正态分布（均值0，标准差1）
    
    randint(low[,high,shape,dtype])   返回在[0,low)或[low,high)中生成的随机整数
    
    random([shape])                   返回的随机数值在[0.0,1.0)
    
    choice(arr[,shape])               返回的随机值在arr数组中生成
                                      若arr为一个数，则从range(arr)中生成
                                      
    shuffle(arr)                      将arr数组进行随机排列，修改原数组，无返回值
                                      若arr是多维数组，则只会在第一维度打散数据。例如对二维数组，只会打乱行的次序
                                      
    permutation(arr)                  将arr数组进行随机排列，不修改原数组，返回一个新数组
                                      若arr为一个数，则生成range(arr)的随机排列
                                      若arr是多维数组，则只会在第一维度打散数据
                                      
    normal([loc,scale,shape])         返回的随机数值是按照平均值loc和标准差scale生成的高斯分布的数字
    
    uniform([low,high,shape])         返回的随机数值是从一个均匀分布的[low,high)区间中随机采样
    
    随机数值通常用于添加随机噪声
    
"""
import numpy as np
np.random.seed(666)