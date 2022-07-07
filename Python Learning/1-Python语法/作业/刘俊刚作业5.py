
"""
编写程序实现: 请用户输入用逗号隔开的一串数字, 输出转化成元组后的数据
例如：用户输入  1,2,3,45,678   输出 ("1","2","3","45","678")
"""
"""
print(tuple(input("请分别输入您的出生年月日，并用逗号隔开：").split(sep=",")))
"""

"""
请用4种方式创建一个字典 dic={"name":"Tom", "age":18, "eat":"fish"}
"""
"""
dic1 = {} ; dic1["name"] = "Tom" ; dic1["age"] = 18 ; dic1["eat"] = "fish"
print(dic1)

dic2 = dict(name = "Tom", age = 18, eat = "fish")
print(dic2)

dic3 = dict([("name", "Tom"), ("age", 18), ("eat", "fish")])
print(dic3)

dic4 = dict(zip(["name", "age", "eat"], ["Tom", 18, "fish"]))
print(dic4)
"""

"""
编写程序实现: 请用户分别输入姓名、电话和地址, 并把结果存放到字典中去
"""
"""
dic1 = {"姓名":input("请输入您的姓名："), "电话":input("请输入您的电话："), "地址":input("请输入您的地址：")}
print(dic1)
"""

"""
dic2 = {}
dic2["姓名"] = input("请输入您的姓名：")
dic2["电话"] = input("请输入您的电话：")
dic2["地址"] = input("请输入您的地址：")
print(dic2)
"""

"""
dic3 = dict(姓名 = input("请输入您的姓名："), 电话 = input("请输入您的电话："), 地址 = input("请输入您的地址："))
print(dic3)
"""

"""
dic4 = dict([("姓名", input("请输入您的姓名：")), ("电话", input("请输入您的电话：")), ("地址", input("请输入您的地址："))])
print(dic4)
"""

"""
dic5 = dict(zip(["姓名", "电话", "地址"], [input("请输入您的姓名："), input("请输入您的电话："), input("请输入您的地址：")]))
print(dic5)
"""

