"""Sorting Data"""
"""
    df.sort_values(by=, ascending=)             by参数为字符串或字符串列表，通常为columns，对列排序，也可指定axis
                                                ascending参数为布尔值或布尔值列表，与by参数一一对应，分别指定升序或降序
                                                若指定排序的列中有NaN值，默认排到最后，可指定参数na_position:'first'排第一

    df.sort_index()     按index排序，默认对行排序，或指定axis=1对列排序
                        默认升序排列，或指定ascending=False降序排列
 
    df.nlargest(n,columns)   返回columns列值最大的前n行   
    df.nsmallest(n,columns)  返回columns列值最小的前n行 

"""