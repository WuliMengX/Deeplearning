
""" 
请用户输入身高(m)和体重(kg), 并根据BMI公式(体重/身高的平方)计算出的BMI指数来判断用户的体重情况
判断标准：
BMI >= 35 为重度肥胖
30 <= BMI < 35 为中度肥胖
27 <= BMI < 30 为轻度肥胖
23 <= BMI < 27 为超重
18.5 <= BMI < 23 为正常体重
BMI < 18.5 为轻体重
"""

"""
Hight = float(input("请输入您的身高(m):"))
Weight = float(input("请输入您的体重(kg):"))

if (BMI := Weight / Hight**2) >= 35:
    print("重度肥胖")
elif BMI >= 30 and BMI < 35:            #可以直接写BMI >= 30即可，下同。每个条件语句只会满足一次结果，后面的就不会执行了
    print("中度肥胖")
elif BMI >= 27 and BMI < 30:
    print("轻度肥胖")
elif BMI >= 23 and BMI < 27:
    print("超重")
elif BMI >= 18.5 and BMI < 23:
    print("正常体重")
else:
    print("轻体重")
"""

"""三元表达式：
print("重度肥胖" if (BMI := Weight / Hight**2) >= 35 else "中度肥胖" if BMI >= 30 and BMI < 35 else "轻度肥胖" if BMI >= 27 and BMI < 30 else "超重" if BMI >= 23 and BMI < 27 else "正常" if BMI >= 18.5 and BMI <23 else "轻体重")
"""

""" 
请用户输入三个不同的整数, 输入时用逗号(,)隔开, 利用条件语句判断出这三个整数中的最大值
"""

"""
a,b,c = input("请输入三个不同的整数，用(,)隔开:").split(sep=",")                    

if a >= b:                                                      #转换成整数型再进行比较
    if a >= c:
        print(f"最大的整数为：{a}")
    else:
        print(f"最大的整数为：{c}")
else:
    if b >= c:
        print(f"最大的整数为：{b}")
    else:
        print(f"最大的整数为：{c}")
"""

"""三元表达式：
print(f"最大整数为：{a if a >= b and a >= c else b if b >= a and b >= c else c}")
"""



