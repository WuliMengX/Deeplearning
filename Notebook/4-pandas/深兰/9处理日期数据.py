"""处理日期数据"""
"""
    日期数据类型：
        Timestamp       单个日期数据
        DatetimeIndex   多个Timestamp组成的列表
        
    日期数据属性：
        week    周数 1-52
        month   月份 1-12
        quarter 季度 数字1-4

    处理日期索引的缺失：
        DatetimeIndex = pd.data_range(start=,end=)      生成完整的日期序列，start为起始日期字符串，end为...
        df = df.reindex(DatetimeIndex, fill_value=0)    重新设置刚刚生成的日期序列为索引，缺失日期的数据以0填充
        
        resample方法：  (重新采样)
            DataFrame.resample(rule, how=None, axis=0, fill_method=None, 
                                closed=None, label=None, convention='start',
                                kind=None, loffset=None, limit=None, base=0)
                                
        参数	            说明
        freq	            表示重采样频率，例如‘M'、‘5min'，Second(15)
        how='mean'	        用于产生聚合值的函数名或数组函数，例如‘mean'、‘ohlc'、np.max等，默认是‘mean'，其他常用的值由：‘first'、‘last'、‘median'、‘max'、‘min'
        axis=0	            默认是纵轴，横轴设置axis=1
        fill_method = None	升采样时如何插值，比如‘ffill'、‘bfill'等
        closed = ‘right'	在降采样时，各时间段的哪一段是闭合的，‘right'或‘left'，默认‘right'
        label= ‘right'	    在降采样时，如何设置聚合值的标签，例如，9：30-9：35会被标记成9：30还是9：35,默认9：35
        loffset = None	    面元标签的时间校正值，比如‘-1s'或Second(-1)用于将聚合标签调早1秒
        limit=None	        在向前或向后填充时，允许填充的最大时期数
        kind = None	        聚合到时期（‘period'）或时间戳（‘timestamp'），默认聚合到时间序列的索引类型
        convention = None	当重采样时期时，将低频率转换到高频率所采用的约定（start或end）。默认‘end'   

        以一定的时间间隔重新采样，这样刚好可以忽略跳过缺失的日期时间

"""
