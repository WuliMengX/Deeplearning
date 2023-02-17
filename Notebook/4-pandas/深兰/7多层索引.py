"""分组聚合"""
"""
    参考：
        https://mp.weixin.qq.com/s?__biz=Mzg3ODY2MDAyMQ==&mid=2247493083&idx=1&sn=44fe0db5aa9a004315709da1b8e123dc&chksm=cf12f501f8657c177770b428fc5580871ae090b388156cb560a743fd2a666f7b33f8f14604c4&cur_album_id=1999223975666581509&scene=190#rd
        https://www.youtube.com/watch?v=ipoSjrN0oh0
        
    group分组(Series)，agg聚合(DataFrame)

        df.groupby([column1,...])[column2].agg([function,...])
        
        df.groupby([column1,...]).agg({column2:function,...})
    
    以某一个列为index作为参照，查看其他列的数据，反映它们之间存在的关系
    
"""

"""分层索引"""
"""
    groupby的多层索引：
        df.groupby([column1,...])   此时[column1,...]即为索引列表，从左至右从高到低分层(一级索引,二级索引,...)
        
        多层索引筛选数据：
            df.groupby([column1,...]).loc[column1_value1]   此时index变为了二级索引
            
            df.groupby([column1,...]).loc[(column1_value1,column2_value1)]  多层索引可以用元组的形式   

    DataFrame的多层索引MultiIndex:
        df.set_index([column1,...], inplace=)   效果与group相似，但此时类型是DataFrame
        
        多层索引筛选数据：
            df.loc[(column1_value1,column2_value1)]
            df.loc[([column1_value1,column1_value2,...], [column2_value1,column2_value2,...])]

            索引时用:切片来表示从头到尾所有数据，也可以换成slice(None)
            
    df.reset_index()    重置索引
        
        
"""
