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

    
    
    
"""