# list1 = [1, 2, 3], list2 = [4, 5, 6], 代码实现：把list2中的元素添加到list1中，并对list1进行降序排序
"""
list1 = [1, 2, 3] ; list2 = [4, 5, 6]
list1.extend(list2)
list1.sort(reverse=True)
"""
# list1 = [1, 2], list2 = [3, 4], list3 = [5, 6], 代码实现：把list1, list2作为元素添加到list3中，求list3的长度
"""
list1 = [1, 2] ; list2 = [3, 4] ; list3 = [5, 6]
list3.append(list1) ; list3.append(list2)
print(len(list3))
"""
# list1 = [1, 3, 2, 6, 4], 代码实现：删除反向后的list1中索引为3的元素，并输出该元素
"""
list1 = [1, 3, 2, 6, 4]
list1.reverse()
print(list1.pop(3))
"""
# list1 = [1, 3, 2, 6, 4], 代码实现：删除list1元素中的最大值和最小值
"""
list1 = [1, 3, 2, 6, 4]
list1.remove(sorted(list1).pop())
list1.remove(sorted(list1,reverse=True).pop())
"""
# list1 = [1, 3, 2, 6, 4], 代码实现：删除list1元素中的中位数
"""
list1 = [1, 3, 2, 6, 4]
list1.remove(sorted(list1).pop(int(len(list1) / 2)))
"""
# list1 = [1, 3, 2, 6, 1, 1, 4], 代码实现：求list1最后一个元素1的索引
"""
list1 = [1, 3, 2, 6, 1, 1, 4]
print(len(list1)-1 - list(reversed(list1)).index(1))
"""
