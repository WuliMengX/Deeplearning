
# 定义一个函数，实现功能: 移除字符串中的指定索引位置的字符，返回新的字符串

def deleteStr(str, i):
    L = list(str)
    L.pop(i)
    return ''.join(L)


"""
给你一个整数 n, 请你帮忙计算并输出该整数「各位数字之积」与「各位数字之和」的差

示例 1:
输入: n = 234
输出: 15 
解释:
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15

示例 2:
输入: n = 4421
输出: 21
解释: 
各位数之积 = 4 * 4 * 2 * 1 = 32 
各位数之和 = 4 + 4 + 2 + 1 = 11 
结果 = 32 - 11 = 21
"""


def differofms(n):
    M = 1
    S = 0
    for i in list(n):
        M *= int(i)
        S += int(i)
    return M - S


print(differofms(input("n = ")))
