"""KNN"""
"""
    KNN三要素：
        K值的选择
        距离度量
        分类决策规则：多数表决等
        
    SKlearn-KNN:
        参数：
            fit
            get_params
            kneighbors
            kneighbors_graph
            predict
            predict_proba
            score
            set_params
            
    KNneighborsClassifier参数说明：
        n_neighbors:默认5,即K值，选取最近的K个点
        weight:默认是uniform，参数可以是uniform、distance，也可以是自定义函数
                uniform是均等的权重，所有邻近点权重相等
                distance是不均等的权重，距离近的点影响更大
                自定义函数：接受距离的数组，返回一组维数相同的权重
        metric:距离度量，默认是p=2的欧式距离    #基本不用变
        p:距离度量公式，默认p=2，也可以设置为1使用曼哈顿距离

"""
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np


