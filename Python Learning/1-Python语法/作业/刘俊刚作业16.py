"""
给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。


示例 1: 
输入: low = 3, high = 7
输出: 3
解释: 3 到 7 之间奇数数字为 [3,5,7] 。

示例 2: 
输入: low = 8, high = 10
输出: 1
解释: 8 到 10 之间奇数数字为 [9] 。
"""


def oddnumber(low: int, high: int):
    return len([x for x in range(low, high + 1) if x % 2 != 0])


# print(oddnumber(3, 7))
# print(oddnumber(8, 10))

"""
输出100以内的孪生质数 (孪生质数就是指相差2的质数对, 例如3和5, 5和7, 11和13…)
"""


def Twin__Prime(x: int):
    def if__prime(num: int):
        if num == 2:
            return True
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    lis = [i for i in range(2, x + 1) if if__prime(i)]
    return [(i, i + 2) for i in lis if (i + 2) in lis]


print(Twin__Prime(100))
