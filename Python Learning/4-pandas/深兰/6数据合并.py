"""数据合并"""
"""
    来源：https://mp.weixin.qq.com/s?__biz=Mzg3ODY2MDAyMQ==&mid=2247493106&idx=1&sn=7aefa2284d6db3bf2cceedf5db177aaf&source=41#wechat_redirect
    
    MERGE函数：
    pd.merge(left,   # 待合并的2个数据框
         right, 
         how='inner',  # ‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’
         on=None, # 连接的键，默认是相同的键
         left_on=None,  # 指定不同的连接字段：键不同，但是键的取值有相同的内容
         right_on=None, 
         left_index=False,   # 根据索引来连接
         right_index=False, 
         sort=False, # 是否排序
         suffixes=('_x', '_y'),   # 改变后缀
         copy=True, 
         indicator=False,   # 显示字段来源
         validate=None)

    参数的具体解释为：

        left、right：待合并的数据帧
        how：合并的方式，有5种：{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, 默认是 ‘inner’
            1、 left：左连接，保留left的全部数据；right类似；类比于SQL的left join 或者right join
            2、outer：全连接功能，类似SQL的full outer join
            3、inner：交叉连接，类比于SQL的inner join
            4、cross：创建两个数据帧DataFrame的笛卡尔积，默认保留左边的顺序 
            
        on：连接的列属性；默认是两个DataFrame的相同字段
        left_on/right_on：指定两个不同的键进行联结
        left_index、right_index：通过索引进行合并
        suffixes：指定我们自己想要的后缀 
        indictor：显示字段的来源

    来源：https://mp.weixin.qq.com/s?__biz=Mzg3ODY2MDAyMQ==&mid=2247493109&idx=1&sn=6cf7ba6f16e884c7830f08568748d02d&chksm=cf12f52ff8657c39c0dc4248befbfcbb8afb58fa42939f8f6a1c79ad54e723619ac2f1a49c21&cur_album_id=1999223975666581509&scene=190#rd
    
    CONCAT函数：
    pandas.concat(objs,  # 合并对象
              axis=0,   # 合并方向，默认是0纵轴方向
              join='outer', # 合并取的是交集inner还是并集outer
              ignore_index=False, # 合并之后索引是否重新
              keys=None, # 在行索引的方向上带上原来数据的名字；主要是用于层次化索引，可以是任意的列表或者数组、元组数据或者列表数组
              levels=None, # 指定用作层次化索引各级别上的索引，如果是设置了keys
              names=None, # 行索引的名字，列表形式
              verify_integrity=False, # 检查行索引是否重复；有则报错
              sort=False, # 对非连接的轴进行排序
              copy=True   # 是否进行深拷贝
             )

    JOIN方法：
    dataframe.join(other,  # 待合并的另一个数据框
        on=None,  # 连接的键
        how='left',   # 连接方式：‘left’, ‘right’, ‘outer’, ‘inner’ 默认是left
        lsuffix='',  # 左边（第一个）数据框相同键的后缀
        rsuffix='',  # 第二个数据框的键的后缀
        sort=False)  # 是否根据连接的键进行排序；默认False

    APPEND方法：
    DataFrame.append(other, 
                 ignore_index=False, 
                 verify_integrity=False, 
                 sort=False)    
    
    参数解释：
        other：待合并的数据。可以是pandas中的DataFrame、series，或者是Python中的字典、列表这样的数据结构
        ignore_index：是否忽略原来的索引，生成新的自然数索引
        verify_integrity：默认是False，如果值为True，创建相同的index则会抛出异常的错误
        sort：boolean，默认是None。如果self和other的列没有对齐，则对列进行排序，并且属性只在版本0.23.0中出现。


"""