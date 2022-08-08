"""概述"""
"""
    TF-IDF:(term frequency–inverse document frequency)
        词条的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降
        
        TF  词频 
            词条在所有文本（语料库或训练数据集）中出现的次数
            一般会归一化处理（该词条数量/该文档中所有词条数量）
        
        IDF 逆向文件频率
            指一个词条重要性的度量
            lg(语料库中总文件数目/包含该词语的文件数目) 越大越重要
            通常会带一个平滑系数，防止除数为0
            
        TF-IDF = TF * IDF

    在训练数据集上运行模型（算法）并在测试数据集中测试效果，迭代进行数据模型的修改，这种方式被称为交叉验证
        （训练集构建模型，测试集评估模型）
        
    分类算法中常见模型测试评估指标：
        准确率Accuracy：提取出的正确样本数/总样本数 
        召回率Recall：正确的正例样本数/样本中的正例样本数--覆盖率
        精准率Precision：正确的正例样本数/预测为正例的样本数
        F值：Precision*Recall*2/(Precision+Recall) 精准率和召回率的调和平均值
        
        *混淆矩阵    
        ROC(Receiver Operating Characteristic)：分类混淆矩阵中FPR-TPR两个量之间的相对变化情况
            当正负样本不平衡时，这种模型评价方式比起一般的精确度评价方式好处尤其显著
            
        AUC(Area Under Curve)：ROC曲线下的面积
            AUC的值越大越好，0.5<AUC<1时优于随机猜测
            
    回归结果度量：
        平均平方误差MSE
        平均平方根误差RMSE     
        平均绝对误差MAE
        R2        
"""
from sklearn.metrics import precision_score # 精确度
from sklearn.metrics import recall_score # 召回率
from sklearn.metrics import f1_score # F值
from sklearn.metrics import confusion_matrix # 混淆矩阵
from sklearn.metrics import roc_curve # ROC
from sklearn.metrics import auc # AUC

from sklearn.metrics import mean_absolute_error # MAE
from sklearn.metrics import mean_squared_error # MSE
from sklearn.metrics import r2_score # R2