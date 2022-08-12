"""KNN"""
"""
    有监督学习
    KNN三要素：
        K值的选择 k过小时误差小，模型复杂过拟合；k过大时相反
        距离度量 一般使用欧氏距离
        分类决策规则：分类预测用(加权)多数表决 回归预测用(加权)平均值法
        
    原理：
        1.训练集中获取K个离待预测样本距离最近的样本数据
        2.根据获取得到的K个样本数据来预测当前待预测样本的目标属性值(label)
    
    训练KNN模型需要进行特征标准化操作：
        在距离度量时，如果不进行特征标准化，那么个样本间的距离会相差较大
        依赖权重和距离度量的算法需要进行特征处理。
        
   算法实现方式：
    KNN算法的重点在于找出K个最邻近点，主要方式有：
        
        蛮力实现 brute:计算预测样本到所有训练集样本的距离，然后选择最小的k个距离即可得到k个最邻近点，算法效率低
        
        KD树 ：首先对训练数据建模，构建KD树，然后再根据建好的模型来获取临近样本数据 
        
    此外，还有一些从KD树修改后的求解最邻近点的算法，比如Ball Tree、BBF Tree、MVP Tree等

    KD树构建方式：
        分别计算n个特征取值的方差，用方差最大的第k维特征作为根节点
        对于这个特征，选择其取值的中位数作为样本的划分点。小于该值的样本划分到左子树，其余划分到右子树。（一半一半）
        对左右子树采用同样的方式找方差最大的特征作为根节点，递归即可产生KD树
        
    KD树查找最近邻 不太理解
        
"""