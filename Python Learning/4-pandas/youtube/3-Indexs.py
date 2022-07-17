"""Set Reset and Use Indexes"""
"""
    默认行索引index是int range
    df.set_index(lable,inplace) 设置lable的value range为行索引，inplace=True时修改df，默认False
    df.reset_index(inplace)     重置index为默认

    读取文件时可设置默认index
    df = pd.read_csv("文件路径",index_col=lable)    效果与set_index相同
    
    df.sort_index(ascending，inplace) 对index进行排序，ascending=False时降序排列，默认True升序
    
"""