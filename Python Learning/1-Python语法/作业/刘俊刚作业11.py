
# 定义一个函数，实现功能: 移除字符串中的指定索引位置的字符，返回新的字符串

def deleteStr(string: str, i: int):
    """移除字符串中的指定索引位置的字符，返回新的字符串"""
    L = list(string)
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


def differofms(n: int):
    """返回传入的整数各位数字之积与各位数字之和的差"""
    pdt = 1
    sum = 0
    for i in str(n):
        pdt *= int(i)
        sum += int(i)
    return pdt - sum


print(differofms(int(input("n = "))))
