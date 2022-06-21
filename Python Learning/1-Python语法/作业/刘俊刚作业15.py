"""
给你一个整数 x , 如果 x 是一个回文整数, 返回 True ；否则, 返回 False 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如, 121 是回文, 而 123 不是。
"""


def func(x: int):
    if x == int("".join(reversed(list(str(x))))):
        return True
    else:
        return False


# x = int(input("输入整数："))
# print(func(x))


"""
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

1000以内的阿姆斯特朗数:  1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

检测用户输入的数字是否为阿姆斯特朗数: 
"""


def if_Armstrong_number(x: int):
    s = 0
    for i in str(x):
        s += int(i)**len(str(x))
    if s == x:
        return True
    else:
        return False
    
# x = int(input("输入正整数n:"))
# print(if_Armstrong_number(x))
