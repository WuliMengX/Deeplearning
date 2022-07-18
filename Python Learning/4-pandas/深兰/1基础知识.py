"""基础知识"""
"""
    数据类型：
        Series对象    Series = pd.Series(values, index, name, dtype)
        
            取出元素：Series[index]    取出多个indexes为列表
        
            访问属性：Series.index; Series.name; Series.dtype
            
            调用方法：Series.function()
            
        DataFrame对象    DataFrame = pd.DataFrame(values, index)  
        
            values的形式为字典：{column:series,...}
            
            取出一列为Series：df.[column]   取出多列columns为列表
            
            访问属性：df.index; df.columns; df.values; df.shape;
            
            调用方法：df.function()
            
            修改行名或列名：df.rename(index={old:new}, columns={old:new})
        
            索引对齐特性：多个df对象进行运算时，它们的索引会被自动对齐，运算时使用的是对齐后的数据进行操作
            
            删除列：
                1.df.drop(columns=, index=, inplace=) 若添加index参数会删除对应行
                2.def df[column]
                3.df.pop(column)    同时返回被删除的列Series
            添加列：
                1.df[new_column] = series        new_column是原DF对象没有的columns
                2.df.assign(new_column=Series)   assign不会对原DF对象修改
                
            根据类型选择：df.select_dtype(include=[dtype])  dtype参数可以是'number'、'float'等
            
            to_frame方法可以将Series转换成DataFrame对象：
                Series.to_frame()
                Series.to_frame().T     转置操作T
                
            常用函数：
                df.head()      
                df.tail()
                df[columns].unique()            返回唯一值列表
                df[columns].nunique()           返回唯一值的个数
                df[columns].count()             返回非缺失值元素个数
                df[columns].value_counts()      返回各个唯一值元素的个数
                df.info()                       
                df.describe()                   默认统计数值型数据的各个统计量，对非数值型也可以用
                df[columns].idxmax()            返回最大值所在的index
                df[columns].clip(low,high)      小于low的变为low，大于high的变为high，保留[low,high]内的数据
                df[columns].replace([old,new],[old,new]) 将各个old替换为new
                df.replace({column:{old:new, old:new}})  字典的形式
            
            排序：
                df.sort_values(by=, ascending=)     by参数为字符串或字符串列表，通常为columns，对列排序，也可指定axis
                                                    ascending参数为布尔值或布尔值列表，与by参数一一对应，分别指定升序或降序
                                                    若指定排序的列中有NaN值，默认排到最后，可指定参数na_position:'first'排第一

                df.sort_index()     按index排序，默认对行排序，或指定axis=1对列排序
                                    默认升序排列，或指定ascending=False降序排列
                
                df.nlargest(n,columns)   返回columns列值最大的前n行   
                df.nsmallest(n,columns)  返回columns列值最小的前n行 
                                         
"""