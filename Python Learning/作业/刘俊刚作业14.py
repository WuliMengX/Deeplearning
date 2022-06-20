
# 实现最大公约数算法（只考虑正整数）

from functools import reduce


def numsInput(): return [int(x)
                         for x in input("依次输入数组的元素，用逗号隔开：").split(sep=",")]


def GCD(nums):

    def ifcommondivisor(n: int):  # 构建一个函数判断参数n是否为数组所有元素的公约数
        for i in nums:            # 局部作用域可以调用Enclosing变量nums
            if i % n != 0:
                return False
        return True

    # filter函数返回[1,min(nums)]范围内属于公约数的整数组成的可迭代对象
    return max(filter(ifcommondivisor, list(range(1, min(nums)+1))))


# nums = numsInput()
# print(GCD(nums))


# 实现最小公倍数算法（只考虑正整数）


def LCM(nums):

    def LCM_of_TWO(a: int, b: int):   # 构建一个函数用公式法求两个数的最大公倍数
        return a*b // GCD([a, b])     # 两个数的乘积等于这两个数的最大公约数与最小公倍数的积

    return reduce(LCM_of_TWO, nums)   # 调用reduce函数求两个或两个数以上的最大公倍数


# nums = numsInput()
# print(LCM(nums))
