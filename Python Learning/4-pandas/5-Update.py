"""Update rows and columns"""
"""
    df.columns是一个series对象，也是一个可迭代对象：
        若series对象内的数据类型是object即字符串，可用以下方法修改原数据：
        修改多个lable：
            df.columns = [x,y,z,...]    为多个lables赋予新的值
            df.columns = [x.upper() for x in df.columns] 
            df.columns.str.replace('_',' ')     
            df.columns = df.apply(函数名)
            df.rename(columns = {old1:new1,...},inplace)
        
        指定行和lable进行修改：
            df.loc[index,lable] = [x,y,z,...]
            若是单个值也可用：df.at[index,lable] = x
            
        注意：
            使用filt筛选过滤来修改时必须用loc：
            df[filt][lable]    修改的方式会报错
            df.loc[filt,lable] 则不会报错    
            
        指定列修改（整列修改）：
            df[lable] = df[lable].str.upper()
            df[lable] = df[lable].apply(upper) 
                
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