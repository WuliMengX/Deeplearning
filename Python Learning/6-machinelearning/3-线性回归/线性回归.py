"""3-线性回归"""
"""
    越复杂的模型越容易过拟合
    
        过拟合：模型在训练集上表现好，测试集上表现差的现象
    
        正则：限制可行解空间，防止过拟合
            经验风险加上一个正则化项，模型越复杂，正则化值就越大
            作用是选择经验风险和模型复杂度同时较小的模型
            
    回归：
        目的：回归预测数值型的目标值
        定义：求回归方程的回归系数(权重)的过程就是回归
        具体方法：用回归系数乘以输入值，再将结果全部加在一起得到预测值
    
    线性回归的前提是数据具有一定的线性特点，简单方法就是用可视化观察数据（散点图）
    
    算法：最小二乘法 误差的平方最小化
    
    回归算法的评价：
        MSE均方误差：       不推荐，因为带平方所以量纲与原数据不同
        RMSE均方根误差      实质为MSE开根号，推荐，能放大错误率
        MAE平均绝对误差     推荐
        R-Squared准确率    from sklearn.metrics import r2_score
                           r2_score(X_test,y_test)
    
    大多数情况下，应该避免使用纯线性回归，岭回归是个不错的默认选择
    如果实际用到的特征只有少数几个，倾向于使用Lasso回归或者弹性网络，因为它们会将无用的特征权重降为0
    一般弹性网络优于Lasso回归。特征数量超过样本数或几个特征强相关的时候Lasso回归表现不稳定
    
"""
"""参考代码"""
# from sklearn.datasets import load_boston
# from sklearn.linear_model import LassoCV, ElasticNetCV

# boston = load_boston()
#
# lscv = LassoCV(alphas=[1.0, 0.1, 0.01, 0.001, 0.005, 0.0025, 0.001, 0.00025], normalize=True)
#
# lscv.fit(boston.data, boston.target)
#
# print('Lasso optimal alpha:%.3f' % lscv.alpha_)
#
# encv = ElasticNetCV(alphas=[1.0, 0.01, 0.005, 0.0025, 0.001], l1_ratio=(0.1, 0.25, 0.5, 0.75, 0.9), normalize=True)
#
# encv.fit(boston.data, boston.target)
#
# print('ElasticNet optimal alpha:%.3f and L1 ratio:%.4f' % (encv.alpha_, encv.l1_ratio_))

