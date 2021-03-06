"""
给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。


示例 1：
输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始

示例 2：
输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对
"""
def numsInput(): return [int(x)
                         for x in input("依次输入数组的元素，用逗号隔开：").split(sep=",")]


def good_number_count(nums: list):
    i = 0
    count = 0
    for x in nums:
        for y in nums[i+1:]:
            if x == y:
                count += 1
        i += 1
        if i == len(nums) - 1:
            return count

nums = numsInput()
print(good_number_count(nums))
    
  

"""
给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。

子字符串 是字符串中的一个连续字符序列。


示例 1：
输入：s = "aa"
输出：0
解释：最优的子字符串是两个 'a' 之间的空子字符串。

示例 2：
输入：s = "abca"
输出：2
解释：最优的子字符串是 "bc" 。

示例 3：
输入：s = "cbzxy"
输出：-1
解释：s 中不存在出现出现两次的字符，所以返回 -1 。

示例 4：
输入：s = "cabbac"
输出：4
解释：最优的子字符串是 "abba" ，其他的非最优解包括 "bb" 和 "" 。
"""

def lonest_string(string):
    i = 0
    count = -1
    for x in string:
        if (j := string.rfind(x)) != -1 and j - i - 1 > count:
            count = j - i - 1
        i += 1
    return count

# string = input("请输入字符串:")
# print(lonest_string(string))