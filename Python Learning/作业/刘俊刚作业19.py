"""
全字母句 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。

如果是，返回 True ；否则，返回 False 。


示例 1：
输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
输出：true
解释：sentence 包含英语字母表中每个字母至少一次。

示例 2：
输入：sentence = "lceftczdef"
输出：False
"""


from numpy import copy


def all_alphabet(sentence: str):
    if len(sentence) < 26 or not sentence.isalpha:
        return False
    if len(set(sentence.lower())) == 26:
        return True
    else:
        return False


# sentence = input("sentence = ")
# print(all_alphabet(sentence))


"""
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？输出所有组合？
"""

def three_list(lis: list):
    
    return {(i[0],i[1],j) for i in [[x, y] for x in lis for y in lis if x != y] for j in lis if j != i[0] and j != i[1]}
    
    
print(three_list([1,2,3,4]),f"共有{len(three_list([1,2,3,4]))}种组合")

