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

"""数据转换"""
"""
    数据转换函数对比：map、apply、applymap：
        1. map：只用于Series，实现每个值->值的映射；
        2. apply：用于Series实现每个值的处理，用于Dataframe实现某个轴的Series的处理；
        3. applymap：只能用于DataFrame，用于处理该DataFrame的每个元素；

    map用于Series值的转换
        Series.map(dict)        dict的形式为{old:new,...}
        Series.map(function)    function处理的参数为Series的每一个元素
        
    apply用于Series和DataFrame的转换    
        Series.apply(function)              函数的参数是每个值
        DataFrame.apply(function,axis=)     函数的参数是对应轴的Series

    applymap用于DataFrame所有值的转换
        df.applymap(function)   function处理的参数为df的每一个元素
        
        
        map() apply() applymap()三个函数：
    
        map(函数名或匿名函数表达式):
            将一个自定义函数作用于Series对象的每个元素，Series对象特有，必须对所有元素都操作到
            例如df["first"] = df["first].map({'Corey':'chris','Jane':'Mary'})
            但这里只替换了一部分，没有操作到的元素会变为NaN，不想这样的后果，此时可以使用replace
            df["first] = df["first].replace({'Corey':'chris','Jane':'Mary'})
            
        apply(函数名或匿名函数表达式)：
            整个DataFrame对象上任意一列或多列，或者一行或多行，即可在任意轴操作
            在一列使用apply时，效果跟map一样，多列时只能用apply
            实质上apply是对一到多个Series对象进行操作，但如果操作的是DataFrame整个时，例如df.apply(len)
            是对df.Columns的每一个lable整体操作，返回值是每一个lable有多少个元素
            
        applymap(函数名或匿名函数表达式):
            将自定义函数作用于DataFrame的所有元素，自定义函数要根据元素的数据类型来使用
            比如元素是object，df.applymap(str.lower)而不是lower，以上的apply和map都要注意这一点

"""