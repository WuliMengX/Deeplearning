
""" 把下面print输出的内容, 改为3种字符串格式化方式分别表示 """

name = "张三"
age = "18"
time = "7.5"
print("我是", name, ", 我今年", age, "岁了, ", "明年我", int(age)+1, "岁!", sep="")


# %格式化
print("我是%s, 我今年%s岁了, 明年我%d岁!" % (name,age,int(age)+1))


# format格式化
print("我是{}, 我今年{}岁了, 明年我{}岁!".format(name,age,int(age)+1))


# f-string格式化
print(f"我是{name}, 我今年{age}岁了, 明年我{int(age)+1}岁!")





""" 索引和切片考查: 请手动作答, 不要借助Python IDE """

# string = "hello world"，如何切片可以输出 "hello w" ？
"""print(string[:7])"""



# string = "hello world"，如何切片可以输出空格字符 ？
"""print(string[4,5])"""



# string = "hello world"，如何切片可以输出 "d" ？
"""print(string[-1,-2]"""



# string = "hello world"，string[: 6]的结果是什么 ？
"""hello """



# string = "hello world"，string[1 : 8 : 2]的结果是什么 ？
"""el o"""



# string = "hello world"，string[-2 : 3 : -2]的结果是什么 ？
"""lo """

