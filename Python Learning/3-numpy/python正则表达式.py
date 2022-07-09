"""正则表达式"""
"""
    元字符：
    
    .	    匹配除换行符以外的任意字符
    \w	    匹配所有普通字符(数字、字母或下划线)
    \s	    匹配任意的空白符
    \d	    匹配数字
    \n	    匹配一个换行符
    \t	    匹配一个制表符
    \b	    匹配一个单词的结尾或分界
    \B      匹配非单词边界 这个会匹配到位置，而不是字符
    ^	    匹配字符串的开始位置
    $	    匹配字符串的结尾位置
    \W	    匹配非字母或数字或下划线
    \D	    匹配非数字
    \S	    匹配非空白符
    a|b	    匹配字符 a 或字符 b
    ()	    正则表达式分组所用符号，匹配括号内的表达式，表示一个组。
    [...]	匹配字符组中的字符
    [^...]	匹配除了字符组中字符的所有字符
   
    
    量词：
    
    *	    重复零次或者更多次
    +	    重复一次或者更多次
    ？	    重复0次或者一次
    {n}	    重复n次
    {n,}	重复n次或者更多次
    {n,m}	重复n到m次
    
    字符组：
    
    [0123456789]	8	True	在一个字符组里枚举所有字符，字符组里的任意一个字符和"待匹配字符"相同都视为可以匹配。
    [0123456789]	a	False	由于字符组中没有 "a" 字符，所以不能匹配。
    [0-9]	        7	True	也可以用-表示范围，[0-9] 就和 [0123456789] 是一个意思。
    [a-z]	        s	True	同样的如果要匹配所有的小写字母，直接用 [a-z] 就可以表示。
    [A-Z]	        B	True	[A-Z] 就表示所有的大写字母。
    [0-9a-fA-F]	    e	True	可以匹配数字，大小写形式的 a～f，用来验证十六进制字符。
    
    贪婪模式非贪婪模式：
    正则表达式默认为贪婪匹配，也就是尽可能多的向后匹配字符，比如 {n,m} 表示匹配前面的内容出现 n 到 m 次（n 小于 m）
    在贪婪模式下，首先以匹配 m 次为目标，而在非贪婪模式是尽可能少的向后匹配内容，也就是说匹配 n 次即可。

    贪婪模式转换为非贪婪模式的方法很简单，在元字符后添加“?”即可实现，如下所示：
        *	*?
        +	+？
        ？	??
        {n,m}	{n,m}？
        
    正则表达式转义：
    如果使用正则表达式匹配特殊字符时，则需要在字符前加\表示转意。常见的特殊字符如下：
        * + ? ^ $ [] () {} | \
    
    分组和引用：
    捕获分组        (ABC)
    命名捕获分组    (?<name>ABC)
    非捕获分组      (?:ABC)
    数字引用分组    匹配捕获分组的结果 例如，\1 匹配第一个捕获分组的结果，\3 则匹配第三个结果
        
    替换：
    $&      插入匹配到的文本
    $1      插入匹配到的指定分组
    $`      插入匹配到的文本之前的字符串
    $'      插入匹配到的文本之后的字符串
    $$      插入美元符号（$）
    
    标识：
     
    标识符用法：
    例：在compile("正则表达式",re.I) 正则表达式不区分大小写
    
    i       让整个表达式对大小写不敏感
    g       保留上次匹配结果的位置，允许子序列从上次匹配的结果继续搜索
    m       当启用 multiline标识时，使用起始和结尾锚（^ 和 $）会匹配到行首和行尾, 而不是整个字符串的头部和尾部
    y       只会从lastIndex位置开始匹配，且如果设置了全局标识(g）的话会被忽略
    s       点（.）会匹配任何字符，包括换行符
    
    正向先行断言：(?=表达式)，指在某个位置向右看，表示所在位置右侧必须能匹配表达式，表达式不在提取内容内
        (?=.*?[a-z])(?=.*?[A-Z]).+ 这段正则表达式规定了匹配的字符串中必须包含至少一个大写和小写的字母
    
    反向先行断言(?!表达式)的作用是保证右边不能出现某字符
    
    正向后行断言：(?<=表达式)，指在某个位置向左看，表示所在位置左侧必须能匹配表达式
    
    反向后行断言：(?<!表达式)，指在某个位置向左看，表示所在位置左侧不能匹配表达式
    
"""

"""引入python正则表达式的库：import re"""
"""
    match(pattern, string, flag=0)
    函数描述：只从字符串的最开始与pattern进行匹配
             匹配成功返回匹配对象(只有一个结果)，否则返回None            
    pattern是re.compile("正则表达式")的返回值
    然后再调用re.match(patter,string,flag=0)返回与pattern字符串的匹配结果
    
    search(pattern, string, flag=0)
    函数描述：与match()工作方式一样，但是search不是从最开始匹配，而是从任意位置查找第一次匹配到的内容
             如果所有的字符串都没有匹配成功，返回None，否则返回匹配对象
             
    findall(pattern, string[, flags])
    函数描述：查找字符串中所有出现的正则表达式模式，并返回一个匹配列表
    
    group(num=0)
    方法描述：匹配对象的方法，不带参数则返回整个的匹配对象，带参数则返回指定的正则表达式中的分组（引用）匹配对象
             group(1)指定正则表达式中第一个分组（即第一个()括号里的内容，pattern1）
             group(2)指定正则表达式中第二个分组（即第二个()括号里的内容，pattern2），以此类推
    groups(default=None)
    方法描述：返回一个含有所有匹配子组(patternN)的元组，匹配失败则返回空元组
    
    
    
"""
# s1 = "我12345abcde"
# s2 = "12345abcde"

# pattern = re.compile("\w+")

# result1 = re.match(pattern,s1)
# result2 = re.match(pattern,s2)

# result1 = re.search(pattern,s1)
# result2 = re.search(pattern,s2)

# result1 = re.findall(pattern,s1)
# result2 = re.findall(pattern,s2)

# result1 = re.match(pattern,s1).group([1,2,...])  #返回匹配的字符串
# result2 = re.match(pattern,s1).start()  #返回匹配开始的位置 下标
# result3 = re.match(pattern,s1).end()    #返回匹配结束的位置 下标
# result4 = re.match(pattern,s1).span()   #返回一个元组，包含匹配开始和结束的位置

# print(result1)
# print(result2)

"""练习"""
import re
# nameList = ["Satoshi Nakamoto",
#             "Alice Nakamoto",
#             "RoboCop Nakamoto",
#             "satoshi Nakamoto",
#             "Mr. Nakamoto",
#             "Nakamoto",
#             "Satoshi nakamoto"]

# for i in nameList:
#     pattern = re.compile("[A-Z]\w+\sNakamoto$")
#     result = re.match(pattern,i)
#     print(result)
    
wordList = ["Alice eats apples.",
            "Bob pets cats.",
            "Carol throws baseballs.",
            "Alice throws Apples.",
            "BOB EATS CATS.",
            "RoboCop eats apples.",
            "ALICE THROWS FOOTBALLS.",
            "Carol eats 7 cats."]

for i in wordList:
    pattern = re.compile("(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$",re.I)
    result = re.match(pattern,i)
    print(result)