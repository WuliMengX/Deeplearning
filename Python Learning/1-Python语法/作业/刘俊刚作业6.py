
"""
实现一个程序:
用户输入一串小写的英文字母, 输出其中英文字母有几种？

例如： 
输入 abcdcdghopp    输出 8
解释：其中有 a b c d g h o p 八种英文字母
"""

print(len(set(input("请输入一串小写的英文字母："))))







"""
有如下两个列表:
lst1 = [1, 2, 3, 2, 5, 1, 2]
lst2 = [2, 7, 9, 5]

编程实现：
1. 求哪些整数既在lst1中，也在lst2中?
2. 求哪些整数在lst1中，不在lst2中？
3. 求两个列表一共有哪些整数？
"""
lst1 = [1, 2, 3, 2, 5, 1, 2]
lst2 = [2, 7, 9, 5]

print(f"lst1中存在，但lst2不存在的整数有：{set(lst1) - set(lst2)}")        # 差集 set(lst1).difference(set(lst2))
print(f"两个列表都存在的整数有：{set(lst1) & set(lst2)}")                  # 交集 set(lst1).intersection(lst2)
print(f"两个列表中包含的整数有：{set(lst1) | set(lst2)}")                  # 并集 set(lst1).union(set(lst2))




