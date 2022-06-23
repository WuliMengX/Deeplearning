
"""
给你一个字符串 s , 如果 s 是一个 好 字符串, 请你返回 True , 否则请返回 False 。

如果 s 中出现过的 所有 字符的出现次数 相同 , 那么我们称字符串 s 是 好 字符串。


示例 1: 
输入: s = "abacbc"
输出: True
解释: s 中出现过的字符为 'a', 'b' 和 'c' 。s 中所有字符均出现 2 次。

示例 2: 
输入: s = "aaabb"
输出: False
解释: s 中出现过的字符为 'a' 和 'b' 。
'a' 出现了 3 次, 'b' 出现了 2 次, 两者出现次数不同。
"""


from pyparsing import nums


def good_string(string: str):
    return len(set([string.count(i) for i in set(list(string))])) == 1

# string = input("输入字符串:")
# print(good_string(string))


"""
给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。

请你返回 nums 中唯一元素的 和 。


示例 1: 
输入: nums = [1,2,3,2]
输出: 4
解释: 唯一元素为 [1,3] , 和为 4 。

示例 2: 
输入: nums = [1,1,1,1,1]
输出: 0
解释: 没有唯一元素, 和为 0 。
"""


def numsInput(): return [int(x)
                         for x in input("依次输入数组的元素，用逗号隔开：").split(sep=",")]


def only_number(nums: list):
    str_nums = [str(x) for x in nums]
    return sum([int(i) for i in set(str_nums) if "".join(str_nums).count(i) == 1])


nums = numsInput()
print(only_number(nums))
