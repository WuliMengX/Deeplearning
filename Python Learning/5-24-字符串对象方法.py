"""字符串对象方法"""
"""
str.replace(old,new,count)    #将字符串中old字符串替换为new字符串 count默认-1 替换所有能替换的

str.strip(chars)              #chars指定要移除的字符序列 默认移除空白符
                              #从字符串左右两边删除指定的字符序列 会考虑chars的所有组合

str.center(width,fillchar)               #与下类似 返回的字符串中原字符串在其正中
str.ljust(width,fillchar) ; str.rjust()  #width指定返回的字符串长度
                                         #fillchar填充字符 必须是单个字符 默认空格符
                                         #返回长度为width的字符串 原字符串靠左对齐 使用fillchar填充空位

str.partition(sep) ; str.rpartition()    #sep分隔符
                                         #在sep首次出现的位置拆分字符串 返回一个包含三个元素的元组 （"分隔符之前的部分","分隔符本身","分隔符之后的部分"）
                                         #未找到分隔符 返回的元组包含字符串本身以及两个空字符串

str.startswith(prefix,start,end) ; str.endswith()             #prefix匹配前缀 可以是字符、字符串、或者元组（元组中只要一个元素满足即可）
                                                              #判断字符串是否以指定的prefix开始 返回true或false

str.isalnum() ; str.isalpha() ; str.isdigit() ; str.isspace() #判断字符串所有字符是否都为字母、文字或数字
                                                              #字母、数字、空白符
                                                              #返回true或false

str.split(sep=None,maxsplit=-1) ; str.rsplit()                #sep是分割字符串的分隔符 默认为所有空白符
                                                              #maxsplit最大分割次数 默认-1 分隔所有
                                                              #指定分隔符对字符串进行分割 返回字符串列表 返回结果不包括分隔符

str.join(iterable)            #iterable包括字符串、列表[,]、元组(,)、字典{:}、 集合{,} 返回字符串
                              #用str（指定字符）连接iterable对象中的元素（必须是字符串类型）
                              #字典只取键，不取值 
                              #集合无序，所以返回结果不确定

str.count(sub,start,end)                 #返回子字符串在字符串中出现的次数 默认全局搜索

str.find(sub,start,end) ; str.rfind()    #从左第一次找到子字符串时的索引，找不到返回-1，start和end可不填
str.index(sub,start,end) ; str.rindex()  #从右
                                         #index与find类似 但index找不到就会报错 其他一样

str.capitalize()                         #首字母变大写 其他变小写 返回字符串
str.title()                              #所有单词首字母变大写 其他变小写 
str.upper()                              #所有字符变大写 
str.lower()                              #所有字符变小写 
str.swapcase()                           #所有字符大写变小写 小写变大写

"""


