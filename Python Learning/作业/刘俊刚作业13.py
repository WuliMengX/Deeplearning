"""
给你一个数组 nums , 数组中有 2n 个元素, 按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1, y1, x2, y2,..., xn, yn] 格式重新排列, 返回重排后的数组。

示例 1: 
输入: nums = [2, 5, 1, 3, 4, 7], n = 3
输出: [2, 3, 5, 4, 1, 7] 
解释: 由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 , 所以答案为 [2, 3, 5, 4, 1, 7]

示例 2: 
输入: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
输出: [1, 4, 2, 3, 3, 2, 4, 1]

示例 3: 
输入: nums = [1, 1, 2, 2], n = 2
输出: [1, 2, 1, 2]
"""

def numsInput(): return [int(x) for x in input("依次输入数组的元素，用逗号隔开：").split(sep=",")]  # 列表推导式

def sortnums(nums: list, n: int):
    if n == 1:
        return nums
    else:
        i = 0
        while True:
            nums.insert(2*i+1, nums.pop(n))  # 只对yn进行pop和insert操作
            i += 1
            n += 1
            if n == len(nums) - 1:
                break
        return nums

# print(sortnums(numsInput(), int(input("n = "))))


"""
给你一个数组 nums 。数组「动态和」的计算公式为: runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

示例 1: 
输入: nums = [1, 2, 3, 4]
输出: [1, 3, 6, 10]
解释: 动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

示例 2: 
输入: nums = [1, 1, 1, 1, 1]
输出: [1, 2, 3, 4, 5]
解释: 动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
"""

def runingSum(nums: list): return [sum(nums[:i[0]+1]) for i in list(enumerate(nums))]   #枚举获得下标 通过切片和sum函数获得动态和 用列表推导式返回列表

# print(runingSum(numsInput()))
