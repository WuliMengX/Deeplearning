"""Clean Data"""
"""
    df.dropna([axis=,how=,subset=[columns]])    删除值存在缺失值(None,NaN)的行，可指定axis=1删除列
                                                how参数有any和all，默认any：缺失值出现就删除 all：所有值都缺失才删除
                                                subset参数指定删除columns存在缺失值的行
                                                Series.dropna用法一样
                            
    对于其他并非缺失值但不需要或无意义的值，可以先将值进行替换再删除
        df.replace(string,numpy.nan,inplace=True)  string为不需要或无意义的值 替换为numpy.nan(缺失值None)
    
    检测缺失值后进行填充：
        df.isna()   返回一个boolean DataFrame，检测值是否为缺失值(None,NaN)  
                    函数别名df.null()
        df.fillna(string)   将缺失值替换为string
    
    

"""