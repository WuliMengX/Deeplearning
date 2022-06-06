import random

from scipy import rand

INFO = {0:"石头",1:"剪刀",2:"布"}

computer = random.randint(0,2)
player = int(input("请出拳！输入0代表石头、1代表剪刀、2代表布："))

print(f"电脑出拳：{INFO[computer]}\n玩家出拳：{INFO[player]}")

if computer == player:
    print("平局")
elif player - computer == -1 or player - computer == 2:
    print("玩家胜利！")
else:
    print("电脑胜利！")


"""random 模块常用函数"""
"""
random.random()                         返回[0.0,1.0)内的随机浮点数

random.randint(a,b)                     返回[a,b]内的随机整数

random.uniform(a,b)                     返回[a,b]/[b,a]内的随机浮点数

random.choice(seq)                      从非空序列seq返回一个随机元素。seq为空会引发错误

random.sample(population,k)             从序列或集合中随机获取K个元素，以列表返回（3.9版本集合采样已经弃用）

random.shuffle(x)                       将可变序列x随机打乱位置

random.randrange([start,]stop[,step])   等效于从range(start,stop,step)里随机返回一个元素

random.seed([x])                        起固定随机数的作用，x可以是任意数字：使用相同的x随机数种子生成的随机数值是一样的
"""