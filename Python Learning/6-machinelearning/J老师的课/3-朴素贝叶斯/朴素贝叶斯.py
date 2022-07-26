"""朴素贝叶斯"""
"""
    朴素贝叶斯公式：
        P(A|B) =  P(B|A) * P(A) / P(B)
        
        条件概率：P(B|A) 似然度 两个事件发生之间的关联性
        先验概率：P(A) P(B)
        后验概率：P(A|B) 需要求解的概率
        
        朴素贝叶斯的实质就是求解后验概率来预测的过程，核心方法是通过似然度预测后验概率
        
        推广：多特征分类问题
            
            依据多个特征对样本进行预测分类：
            
                P(类别A1|特征X1，特征X2，特征X3，…) 
                    在特征 X1、X2、X3 等共同发生的条件下，类别 A1 发生的概率，也就是要求解的后验概率
                    
                P(特征X1|类别A1，特征X2，特征X3，…)
                    某个特征的似然度。由于朴素贝叶斯假设特征之间相互独立互不影响，所以可以表示如下：
                    P(特征X1|类别A1)
                
                某个类的后验概率 与 每个特征对于该类的似然度之积(计算得出)乘以该类的先验概率(已知) 正相关 
                后验概率最大的那个类作为最后的预测结果
                
        
    sklearn实现朴素贝叶斯：
        基于贝叶斯定理的算法集中在 sklearn.naive_bayes 包中

        根据对“似然度 P(xi|y)”计算方法的不同，我们将朴素贝叶斯大致分为三种：
            MultinomialNB 多项式朴素贝叶斯      适用于特征是多项式分布
            BernoulliNB   伯努利分布朴素贝叶斯  适用于二项分布
            GaussianNB    高斯分布朴素贝叶斯    适用于特征呈正态分布
                
        算法使用流程
            使用朴素贝叶斯算法，具体分为三步：
            1 统计样本数，即统计先验概率 P(y) 和 似然度 P(x|y)。
            2 根据待测样本所包含的特征，对不同类分别进行后验概率计算。
            3 比较 y1，y2，...yn 的后验概率，哪个的概率值最大就将其作为预测输出
        
"""
#鸢尾花数据集
from sklearn.datasets import load_iris

#导入朴素贝叶斯模型，这里选用高斯分类器
from sklearn.naive_bayes import GaussianNB

#载入数据集
X,y=load_iris(return_X_y=True)
bayes_modle=GaussianNB()

#训练数据
bayes_modle.fit(X,y)

#使用模型进行分类预测
result=bayes_modle.predict(X)
print(result)

#对模型评分
model_score=bayes_modle.score(X,y)
print(model_score)