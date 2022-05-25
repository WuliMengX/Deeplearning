
# name = " gouguoQ   "，代码实现：移除字符串两边的空格，并输出结果
name = " gouguoQ   "
print(name.strip(" "))

# name = " gouguoQ "，代码实现：判断字符串是否以"go"开头，并输出结果
name = " gouguoQ "
print(name.startswith("go"))

# name = " gouguoQ"，代码实现：判断字符串是否以"Q"结尾，并输出结果
name = " gouguoQ"
print(name.endswith("Q"))

# name = " gouguoQ "，代码实现：将字符串中的第一个"o"，替换为"p"，并输出结果
name = " gouguoQ "
print(name.replace("o","p",1))

# name = " gouguoQ "，代码实现：将字符串根据"o"分割，并输出结果
name = " gouguoQ "
print(name.split(sep="o"))

# string = "hello world"，代码实现：请输出字符"l"在字符串中出现的次数
string = "hello world"
print(string.count("l"))

# string = "hello world"，代码实现：请输出字符串中第一次出现字符"l"的索引
print(string.find("l"))


# string = "hello world"，代码实现：请输出字符串中最后一次出现字符"l"的索引
print(string.rfind("l"))


# string = "hello world"，代码实现：将字符串的首字母变成大写，并输出结果
print(string.capitalize())


# string = "hello world"，代码实现：得到字符串为 "h~e~l~l~o~w~o~r~l~d"
print("~".join(string.replace(" ","")))                                                               #replce去掉空格符 
print("~".join("".join(string.split(" "))))                                                           #split去掉空格符，返回的字符串列表用join转换为字符串 
print("~".join(string[:string.find(" ")] + string[string.find(" ")+1:len(string)]))                   #find返回空格符下标，切片拼接去掉空格符
print("~".join(string.partition(" ")[0] + string.partition(" ")[2]))                                  #partition返回分割符为空格符的三元素元组，拼接除分隔符本身元素外的另外两个元素

