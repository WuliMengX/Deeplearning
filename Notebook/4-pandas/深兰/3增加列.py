"""新增数据列"""
"""
    直接赋值创建新列：
        df[new_column]  = Series
        df.loc[:, new_column] = Series
        
    apply方法：
        比如令以上的 ：
            Series = df.apply(function,axis=1)    
            function()是对df的每一行或每一列进行操作，由axis指定
        
    assign方法：
        df.assign(new_column=Series,...) 可同时添加多列
        
    按条件选择分组分别赋值：
        df[new_column] = '' 先创建空列
        df.loc[filt1, new_column] = value1
        df.loc[filt2, new_column] = value2
            

"""