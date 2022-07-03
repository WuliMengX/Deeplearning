"""闭包"""
"""
    闭包的构成条件:
        1.在函数嵌套（函数里面再定义函数）的前提下
        2.内部函数使用了外部函数的变量（参数）
        3.外部函数的返回值是内部函数的引用
        
    闭包如何理解:
        一般来说，如果一个函数结束，函数内部的变量、参数会被释放掉；
        而闭包则不同，它在外部函数结束时，会把内部函数中用到的外部函数的变量、参数保存到内部函数的__closure__属性中，以提供给内部函数使用
"""
# 闭包三要素


# def outer(d: int):

#     a = 3
#     c = 4

#     def inner():
#         b = a + c + d
#         return b

#     return inner


# print(outer(5)())

# inner_f = outer(5)
# print(inner_f.__closure__[0].cell_contents)  # 元组的形式存储
# print(inner_f.__closure__[1].cell_contents)
# print(inner_f.__closure__[2].cell_contents)


def outer():
    funcs = []              
    for k in range(3):
        def inner():
            return k * k
        funcs.append(inner)
    return funcs


""" 这里的f1, f2, f3都是闭包, 本质上都是inner函数, 且使用了outer函数的变量k
    outer函数在结束时, 将变量k保存到内部函数的__closure__属性中,而k最后为2
"""
f1, f2, f3 = outer()
print(f1.__closure__[0].cell_contents)
print(f2.__closure__[0].cell_contents)
print(f3.__closure__[0].cell_contents)
print(f1())
print(f2())
print(f3())
