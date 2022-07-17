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