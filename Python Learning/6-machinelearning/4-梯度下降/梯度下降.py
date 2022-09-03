"""梯度下降法"""
"""
    常用于求解无约束情况下凸函数的极小值，迭代求得逼近值
    某个函数在某点的梯度指向该函数取得最大值的方向，那么它的反反向自然就是取得最小值的方向
    
    步骤：
        1.目标函数J(θ)求解
        2.初始化θ（随机初始化），设置步长α和迭代次数，求J(θ)的导数(梯度)▽J(θ)
        3.沿着负梯度方向迭代，更新后的θ使J(θ)更小，θ=θ-α▽J(θ)
        
    随机梯度下降法（SGD）
        使用单个样本的梯度值作为当前模型参数θ的更新
        
    批量梯度下降法（BGD）
        使用所有样本的梯度值作为当前模型参数θ的更新
        
    小批量梯度下降法（MBGD）
        使用一部分样本的平均梯度作为更新方向
        
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 4, 100) # -6到4之间取100个值
y = x**2 + 2*x + 5
plt.plot(x, y)
plt.show()

x = 3
alpha = 0.8
iteraterNum = 100

for i in range(iteraterNum):
    x = x - alpha * (2*x + 2)

print(x)