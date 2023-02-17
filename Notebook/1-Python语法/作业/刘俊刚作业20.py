"""
给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 合并后的字符串 。


示例 1：
输入：word1 = "abc", word2 = "pqr"
输出："apbqcr"
解释：字符串合并情况如下所示：
word1：  a   b   c
word2：    p   q   r
合并后：  a p b q c r

示例 2：
输入：word1 = "ab", word2 = "pqrs"
输出："apbqrs"
解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
word1：  a   b 
word2：    p   q   r   s
合并后：  a p b q   r   s

示例 3：
输入：word1 = "abcd", word2 = "pq"
输出："apbqcd"
解释：注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。
word1：  a   b   c   d
word2：    p   q 
合并后：  a p b q c   d
"""

def merge_string(word1,word2):
    lis = []
    list1=list(word1)
    list2=list(word2)
    while True:
        lis.append(list1.pop(0))
        lis.append(list2.pop(0))
        if not list1:
            lis.extend(list2)
            return "".join(lis)
        if not list2:
            lis.extend(list1)
            return "".join(lis)
        
        
# word1 = input("请输入word1:")
# word2 = input("请输入word2:")
# print(merge_string(word1,word2))










"""
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。


示例 1：
输入：time = "2?:?0"
输出："23:50"
解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。

示例 2：
输入：time = "0?:3?"
输出："09:39"

示例 3：
输入：time = "1?:22"
输出："19:22"
"""

def latest_time(time_string):
    time_list = list(time_string)
    
    if time_list[0] == '?' and time_list[1] == '?':
        time_list[0:2] = '00'
        
    count = -1
    for i in time_list:
        count += 1
        if i == "?":
            if count == 0:
                time_list[count] = '2'
            elif count == 1:
                if time_list[0] == '2':
                    time_list[count] = '3'
                else:
                    time_list[count] = '9'
            elif count == 3:
                time_list[count] = '5'
            elif count == 4:
                time_list[count] = '9'
    return ''.join(time_list)

# print(latest_time('0?:3?'))






