"""数据统计函数"""
"""
    汇总类：
        df.describe()
        Series.mean()
        Series.max()
        Series.min()
        
    唯一去重：
        Series.unique()
    
    按值计数：
        Series.nunique()
        Series.value_counts()
    
    相关系数和协方差：
        协方差矩阵：    df.cov()    衡量同向反向程度
        相关系数矩阵：  df.corr()   衡量相似度程度
    
        df[column1].corr(df[column2])   单独查看两个变量的相关系数
        
""" 