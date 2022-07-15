"""Grouping and Aggregating"""
"""
    df[columns].median()    返回一列或多列的中位数，忽略NaN值
                            如果是df.median()，会自动返回其中包含数值的列的中位数
                            
    df.describe()   对df中包含数值的列进行数据统计，包含多项数据
    
    df[columns].value_counts(normalize=)  统计列的各个值的计数，默认为个数，normalize=True时为百分比
    
    1.split 2.apply function 3.aggregating
    分组：
        grp = df.groupby([lable])   获取与lable关联的分组
        
        grp.get_group(lable_value)  获取上面分组中lable列的值为lable_value的所有行组成的DataFrame
                                    相当于filt过滤
        
        此时对grp[other_lable]操作，就像对一个lable中的各个值为index，other_lable为columns的DataFrame进行操作
        比如，grp[other_lable].value_counts().loc(lable_value)                          
        
    聚合：
        grp[other_lable].agg([函数名字符串,...])    得到一个以lable的lable_value为index，一或多个函数名为columns组成的DataFrame
                                                   columns每列的数据为原df对象的other_lable列的数据经过函数求得的数据
                                                   
        grp[other_lable].agg([函数名字符串,...]).loc[lable_value]
        
        grp[other_lable].apply(lambda x: x.str.contains(other_lable_value).sum())
    
    
    
"""