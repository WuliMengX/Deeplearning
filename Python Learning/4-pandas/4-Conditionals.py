"""Use Conditionals to Filter"""
"""
    利用逻辑运算符等条件得到bool类型的series对象filt
    通过bool索引可以筛选bool==True的数据
    filt = (df[lable] == index) & (df[lable] == index)
    df[filt,index]
    df.loc[filt,index]
    
    ~filt可以得到bool结果相反的series对象
    
    这里filt是样本数据的过滤器，即筛选行

"""