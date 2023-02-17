# 文件名从小到大排序:  FileName = ["10.py", "2.py", "8.py", "6.py", "100.py"]

FileName = ["10.py", "2.py", "8.py", "6.py", "100.py"]
def Function(string): return int(string.partition('.')[0])


FileName.sort(key=Function)
print(FileName)


"""
给你一个非负整数 num, 请你返回将它变成 0 所需要的步数. 如果当前数字是偶数, 你需要把它除以2; 否则, 减去1

示例 1: 
输入: num = 14
输出: 6
解释: 
步骤 1) 14 是偶数，除以 2 得到 7
步骤 2) 7 是奇数，减 1 得到 6
步骤 3) 6 是偶数，除以 2 得到 3
步骤 4) 3 是奇数，减 1 得到 2
步骤 5) 2 是偶数，除以 2 得到 1
步骤 6) 1 是奇数，减 1 得到 0

示例 2: 
输入: num = 8
输出: 4
解释: 
步骤 1) 8 是偶数，除以 2 得到 4
步骤 2) 4 是偶数，除以 2 得到 2
步骤 3) 2 是偶数，除以 2 得到 1
步骤 4) 1 是奇数，减 1 得到 0
"""


def Founctions(num: int):
    """返回一个非负整数变成0所需要的步数"""
    count = 0
    while num:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num -= 1
            count += 1
    return count


print(Founctions(int(input("输入一个非负整数："))))
