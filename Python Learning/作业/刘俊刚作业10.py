
"""
给你一个字典 dict1 = {'a': 100, 'b':'qwer', 8:300.1} ，计算键和值中所有数字的和
"""


def sum_DictNumber(dit):
    (lis := list(dit.keys())).extend(list(dit.values()))
    s = 0
    for i in lis:
        if type(i) in (int, float, bool, complex):
            s += i
    return s


dct = {'a': 100, 'b': 'qwer', 8: 300.1}
print(sum_DictNumber(dct))

"""
给你一个整数数组 arr, 请你判断数组中是否存在连续三个元素都是奇数的情况: 如果存在，请输出 True ；否则输出 False
示例 1:
输入: arr = [2, 6, 4, 1]
输出: False
解释: 不存在连续三个元素都是奇数的情况

示例 2:
输入: arr = [1, 2, 34, 3, 4, 5, 7, 23, 12]
输出: True
解释: 存在连续三个元素都是奇数的情况，即 [5, 7, 23]
"""


def threeOdds(arr):
    count = 0
    for i in arr:
        if i % 2 != 0:
            count += 1
        else:
            count = 0
        if count == 3:
            print("True")
            return True
    print("False")
    return False


arr1 = [2, 6, 4, 1]
arr2 = [1, 2, 34, 3, 4, 5, 7, 23, 12]
threeOdds(arr2)
