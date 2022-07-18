"""处理缺失值"""
"""
    步骤：
        一、读取文件时，忽略前几个空行
        
            df = pd.read_excel("path", skiprows=N)  skiprows参数忽略前N个空行
            
        二、检测空值
        
            df.isnull()     检测空值，NaN值会返回True，否则为False，对于Series对象也可用
            df.notnull()    检测非空值，与isnull刚好相反
        
        三、删除全是空值的列
        
            df.dropna(axis=1, how='all', inplace=True)
            
        四、删除全是空值的行
        
            df.dropna(axis=0, how='all', inplace=True)     

        五、替换或填充空值
        
            df.fillna({columns:new_values}) 
            
            df.loc[:,column] = df[column].fillna(new_value)
            
        六、保存
        
            df.to_excel("path", index=) 
            index参数的值为True或False，指明是否将index写入文件
            
"""

"""数据排序"""
"""
    Series列排序：
        Series.sort_values(ascending=,inplace=) 默认ascending=True升序
        
    Dataframe列排序：
        df.sort_values(by=,ascending=)  by参数为columns，多个用列表
                                        by参数为多个时，ascending参数也要以列表的形式一一对齐指定升降序
                                        
"""

"""字符串处理"""
"""
    字符串处理仅针对Series对象，且数据类型为字符串
    DataFrame没有str字符串属性和方法，数字列也没有
    
        Series.str.replace(old,new)     替换字符串
        Series.astype()                 转换类型
        Series.str.isnumberic()         判断字符串是否为数字，返回bool型Series
        Series.str.startswith(string)   判断字符串是否以string开头，返回bool型Series
        
        Series.str.slice(0,6)   切片 相当于Series.str[0,6]

"""

"""axis参数的理解"""
"""
    axis=0,计算的对象是一整列上的数据
    axis=1,计算的对象是一整行上的数据

"""

"""index索引的用途"""
"""
    df.set_index(column,inplace=,drop=False)    
        drop参数为False意味着设为index的column依然算作数据中的一列用作计算
        
"""