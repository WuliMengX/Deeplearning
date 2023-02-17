"""查询数据"""
"""
    对于dataframe对象，不能直接索引行，但可以直接索引列：
        df[columns]   columns可以是一个标签或标签列表
        df.columns    效果相同，但不推荐，可能出现命名冲突
        
    iloc[]    只能用下标索引  切片时左闭右开
    loc[]     只能用标签索引  切片时左闭右闭
        df.iloc[arr1,arr2]    arr1和arr2是一个整数或者整数列表 表示下标
        df.loc[index,columns] index和columns是一个标签或者标签列表 表示关键字

        loc条件查询：
            df.loc[filt, :]  返回符合filt条件的所有行组成的DataFrame
            
        loc函数查询：
            df.loc[lambda df:filt, :]   lambda里的df对应的是每一行
            
"""