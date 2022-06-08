# 考察要点: 条件语句、 循环语句
"""
输入一个整数，判断是否为质数

质数就是一个大于1的自然数, 除了1和它本身外, 不能被其他自然数(质数)整除(2, 3, 5, 7等), 换句话说就是该数除了1和它本身以外不再有其他的因数。
"""

"""
intNum = int(input("请输入一个整数："))
if intNum > 1:
    num = intNum - 1
    while True:
        if intNum % num == 0:
            print("这是一个质数！")
        num -= 1
        if num == 1:
            print("这不是一个质数！")
            break
else:
    print("这不是一个质数！")
"""

"""
输入一个非负整数 num, 反复将各个位上的数字相加, 直到结果为一位数。

示例:
输入: 38
输出: 2
解释: 各位相加的过程为: 3 + 8 = 11, 1 + 1 = 2; 由于 2 是一位数, 所以返回 2
"""

"""
num = input("请输入一个非负整数：")
while True:
    sum = 0
    for i in num:
        sum += int(i)
    if sum < 10:
        print(sum)
        break
    else:
        num = str(sum)
"""