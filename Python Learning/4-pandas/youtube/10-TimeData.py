"""Working with Dates and Time Series Data"""
"""
    将非标准格式的日期时间数据转换为标准时间类型datetime64：
        df[lable] = pd.to_datetime(df[lable],format='%Y-%m-%d %I-%p')
        
        lable行的数据为非标准格式的日期时间数据
        format参数通过一一对准让pandas知道原数据的年月日究竟是哪些
    
    d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
    df = pd.read_csv("文件路径", parse_dates=[lable]， data_parser=d_parser)   
        parse_dates参数让pandas知道哪些行的数据是代表时间数据的
        data_parser参数传入一个相当于将非标准时间数据转换为标准时间类型的解码函数
    
    df['Date'].dt.day_name()    返回一个Series，一一对应原数据是星期几
                                Date列的数据为转换过的标准时间类型，day_name指星期几

    df['Date'].min()    最远日期
    df['Date'].max()    最近日期
        两者可以相减运算
           
    filt = (df['Date'] >= '2020')   pandas知道这个2020的含义是年  
                                    如果要更精确可以换成 pd.to_datetime('年-月-日') 
    df.loc[filt]                    筛选出年份大于等于2020的DataFrame

    df.set_index('Date',inplace=True)   甚至可以以时间为index
    df['2019']                          这样筛选可以变得更简单
    df['2020-01':'2020-02']             可以如此使用切片
    df[lable].resample('D').max()       标签为lable的列重新采样，index以天为单位('D')，每一天的最大值
    df.resample('W').mean()             index以周为单位，columns在一周内的平均值
    df.resample('W').agg({lable:'函数名'...})   各个lable的数据各用一个函数处理
      
"""