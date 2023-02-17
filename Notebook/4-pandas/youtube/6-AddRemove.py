"""Add/Remove Rows and Columns Frome DataFrames"""
"""
    Series可以进行字符串操作
    更改原数据添加新列：
        df[new_lable] = df[lable] + string... + df[lable]  不能使用df.lable
                   
        df[[lable1,lable2]] = df[new_lable].str.split(sep, expand=True) 
        
               删除列：
        df.drop(columns=[lable,], inplace=True)


    更改原数据添加新行：
        df.append({lables:values,},ignore_index=True)   没有在字典内的键的值会默认设置位NaN

        df.append(df1, ignore_index=True, sort=False)   对df添加其他df的全部行，lable自动对应
        
               删除行：
        df.drop(index=) index右边也可以是 df[filt].index
        
    pd.concat()连接df对象：
        默认纵向连接，即相当于增加行
        两个df对象的列相同:
            pd.concat([df1,df2])
            连接后的各个df的index不变，若想连接后重新设置index，添加ignore_index=True
            
        两个df对象的列不完全相同：
            pd.concat([df1,df2],sort=false) 列的顺序维持原样 不进行重新排序
            df1中没有而df2中有的列，连接后该列对应df1的值会设置为NaN
            若只想合并相同的列，添加join='inner'参数
            
        设置axis=1，横向连接，相当于增加列
        情况类似    
            
        
"""