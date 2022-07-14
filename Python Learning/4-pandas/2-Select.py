""""Select rows and columns"""
"""
    index和lable分别特指行和列的索引
    
    对于dataframe对象，不能直接索引行，但可以索引列：
        df[lable]   lables可以是一个标签或标签列表
        df.lable    效果相同，但不推荐，可能出现命名冲突
        
    df.columns  返回所有lable组成的一维列表
    
    df.iloc[arr1,arr2]    arr1和arr2是一个整数或者整数列表 表示下标
    df.loc[index,lable]   index和lable是一个标签或者标签列表 表示关键字

    iloc    只能用下标索引  切片时左闭右开
    loc     只能用标签索引  切片时左闭右闭
    
    df[lable].values_counts()   对lable所有出现的值进行统计
    
"""