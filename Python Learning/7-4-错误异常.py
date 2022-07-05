"""错误分类"""
"""
    错误一般可分为两种：
        语法错误：又称解析错误（语法分析器检查到的错误）
        异常：在运行时检测到的错误（程序的语法是正确的）
"""

"""内置异常"""

# import builtins
# print(dir(builtins))

"""处理异常"""
"""
    try ... except ...
        如果在执行 try 子句时没有异常发生，则不会执行 except 子句
        如果 try 子句发生了异常，则跳过该子句中剩下的部分，执行except 子句
        如果 except 子句没有指定异常类型，则可以处理 try 中的所有异常类型
        如果 except 子句指定了异常类型，则只能处理对应的异常类型（指定多个异常类型时，可以用元组来表示）
        如果一个异常没有与任何的 except 匹配，则报错
        
        
    try ... except ... 嵌套
        如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中
        
        
    try ... except ... else ...
        else 子句必须放在所有的 except 子句之后
        else 子句将在 try 子句没有发生任何异常的时候执行
        
    
    try ... except ... as ...
        as 后面为异常实例对象的名称
        
    
    try ... finally ...
        finally 子句将作为 try 语句结束前的最后一项任务被执行
        不论 try 语句是否产生了异常都会被执行
        如果在执行 try 语句时遇到一个 break, continue 或 return 语句，则 finally 子句将在执行 break, continue 或 return 语句之前被执行
        如果 finally 子句中包含一个 return 语句，则返回值将来自 finally子句中的 return 语句的返回值，而非来自 try 子句中的 return 语句的返回值

"""

# def div(a,b):
#     try:
#         c = a / b
#         print(f"{a} / {b} = {c}")
        
#     except ZeroDivisionError as e:  # 相当于e = ZeroDivisionError('division by zero')
#         print(isinstance(e,ZeroDivisionError))
#         print(e)
        
# div(2,0)


"""抛出异常"""
"""
    raise 语句可以主动的抛出异常
    raise 后面可以是 异常实例 / 异常类 / 没有内容
"""

# def div(a, b):
#     if b == 0:
#         raise ZeroDivisionError('除数为0')
#     c = a / b
#     print(f"{a} / {b} = {c}")
    
# # div(2, 1)
# div(2, 0)



"""自定义异常"""
"""
    自定义的异常类通常需要直接或间接的继承 Exception 类
"""

# class MyError(Exception):
#     def __init__(self, message):
#         self.message = message

#     def __str__(self):
#         return str(self.message)


# print(MyError("发生了一个异常"))

"""assert 断言"""
"""
    assert 用于判断一个表达式，在表达式为 False 的时候触发AssertionError 异常
    
    assert expression 等价于if not expression: raise AssertionError
    assert expression [, arguments]等价于：if not expression: raise AssertionError(arguments)
    
    断言成功，继续执行
    断言失败，到此为止
"""
# num = int(input("请输入一个整数: "))
# assert num != 1
# print("断言条件为True, 用户没有输入1")

# num = int(input("请输入一个整数: "))
# assert num != 1, "用户不能输入1"
# print("断言条件为True, 用户没有输入1")

"""
    traceback.format_exc() 返回字符串
    traceback.print_exc()  无返回值，直接输出
    
    其他地方两者相同
"""
# import traceback

# def div(a, b):
#     try:
#         c = a / b
#         print(f"{a} / {b} = {c}")
#     except:
#         traceback.print_exc()
#         print(res := traceback.format_exc())
#         print(type(res))
        
# div('2', 2)





