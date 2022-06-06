"""算术运算符"""
"""
    1.+  加
    2.-  减
    3.*  乘
    4./  除
    5.%  取模
    6.** 幂
    7.// 整除 相当于/再向下取整 注意负数取整 取模
"""

"""比较运算符"""
"""
    返回布尔值:True False
    1.==
    2.!=
    3.>
    4.<
    5.>=
    6.<=
"""

"""赋值运算符"""
"""
    1.=
    2.+=   # a+=3 基本可以理解为 a=a+3 变量也可以是其他数据类型
    3.-=
    4.*=
    5./=
    6.%=
    7.**=
    8.//=
    9.:/        海象赋值运算符 

    海象赋值运算符:可在表达式内部为变量赋值,记得加括号
    优点：减少代码量，不用事先声明中间变量
    
    #写法一:
    string = "hello world"
    length = len(string)
    print(length + 5)
    print(f"string的长度为{length}")

    #写法二：
    string = "hello world"
    print(len(string) + 5)
    print(f"string的长度为{len(string)}")

    #写法三：
    string = "hello world"
    print( ( length := len(string) ) + 5)
    print(f"string的长度为{length}")
    相对写法一 避免了一次赋值给中间变量的步骤
    相对写法二 避免使用两次len()函数

    1.增强赋值:在操作数是一个可变类型对象时会以追加的方式进行处理,普通赋值则以新建的方式处理,此时增强赋值效率更高
    包括:+= -= *= /= %= **= //=

    2.序列赋值:
    a,b = 3,4 等同于(a,b) = (3,4)
    (a,b) = (3,4)
    [a,b] = [3,4]
    a,b,c = [3,4,5]
    a,b,c = "你好吗"

    3.多目标赋值:多个变量都指向同一个数据地址
    a = b = c = 999
    
    4.逻辑运算符:
    and 与 左边为假返回左边,否则返回右边
    or  或 左边为真返回左边,否则返回右边
    not 非 假,返回True;真,返回False

    小知识点:None,False,0,空列表/元组/字典/集合都会被认定为False
    总结: and只要有一边为False,最后结果一定为False;只有两边都为True,最后结果为True
          or 只要有其中一边为True,最后结果为True;只有两边都为False,最后结果才为False

    短路原则:如果前面的部分已经进算出整个表达式的结果,则后面的部分不再计算

    5.成员运算符:返回布尔值,判断对象中是否存在某个元素
    in 和 not in

    6.身份运算符:返回布尔值,判断两个标识符是否引用自相同/或不同对象,类似id(a)==id(b)或id(a)!=id(b)
    is 和 is not

    7.位运算符:把数字看作8bit的二进制来进行计算
    & :  按位与         如果两个相应位都为1,则该位结果为1,否则为0
    | :  按位或         只要两个相应位有一个为1时,结果位就为1
    ^ :  按位异或       只要两个相应位不同,结果就为1
    ~ :  按位取反       对数据的每个二进制位(包括符号位)取反,即把1变为0,0变为1.  ~x值等于-(x+1)
    <<:  左移动         运算数的各二进位全部左移若干位,右边补0
    >>:  右移动         运算数的各二进位全部右移若干位,左边补对应的符号位值

    进制转换函数: 1.bin(x) 将一个整数转变为一个前缀为 0b 的二进制字符串
                 2.hex(x) 将一个整数转变为一个前缀为 0x 的十六进制字符串
                 3.oct(x) 将一个整数转变为一个前缀为 0o 的八进制字符串

    小知识点:     负数在计算机中以原码的补码形式表达
                 负数的反码:对该数的原码除符号位外各位取反
                 负数的补码:对该数的原码除符号位外各位取反,然后再最后一位加1(即反码+1)  
                 正数的反码和补码都与原码相同
                
    + += *的连接操作:可以对字符串 列表 元组进行连接操作(要保证连接对象的类型一致)

    运算符优先级：
        1.幂运算：**
        2.按位取反：~
        3.乘、除、求余、取整
        4.加减法
        5.右移、左移：>> <<
        6.按位与：&
        7.按位异或、或：^ |
        8.比较运算符：<= < > >=
        9.等于运算符：== !=
        10.赋值运算符：= %= /= //= -= += *= **=
        11.身份运算符：is  is not
        12.成员运算符：in  no in
        13.逻辑运算符：not and or
""" 
