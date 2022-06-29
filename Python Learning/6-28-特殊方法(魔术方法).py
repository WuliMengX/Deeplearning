""" 特殊方法（魔术方法）"""
"""
    以两个下划线开头和结尾命名的方法
    特定情况下会被自动调用
    
    __init__(self,[,...])   初始化方法，实例化过程中调用
    
    __call__(self,[,...])   实例对象像函数那样被调用时，会调用该方法---object(参数)
    
    __getitem__(self,key)   执行self[key]操作时，会调用该方法---索引操作 object[n]
    
    __repr__(self) / __str__(self)  实例对象转字符串时，会调用该方法，要求必需返回字符串类型---str(object) print(object) print(f"{object}")
    
    __add__(self, other)    实例对象进行加法操作时会调用该方法，要求实例对象在两对象相加的左边
    
    __radd__(self, other)   实例对象进行加法操作时会调用该方法，要求实例对象在两对象相加的右边，且左边不是实例对象
    
    __sub__(self, other)    实例对象进行减法操作时会调用该方法，要求实例对象在两对象相减的左边
    
    __rsub__(self, other)   实例对象进行减法操作时会调用该方法，要求实例对象在两对象相减的右边，且左边不是实例对象
    
    __mul__(self, other)    实例对象进行乘法操作时会调用该方法，要求实例对象在两对象相乘的左边

    __rmul__(self, other)   实例对象进行乘法操作时会调用该方法，要求实例对象在两对象相乘的右边，且左边不是实例对象

    __truediv__(self, other)    实例对象进行除法操作时会调用该方法，要求实例对象在两对象相除的左边

    __rtruediv__(self, other)   实例对象进行除法操作时会调用该方法，要求实例对象在两对象相除的右边，且左边不是实例对象

    
"""

# class Number:
#     def __init__(self,num):
#         self.num = num

#     def __add__(self,other):
#         return self.num + other #6 + n2 调用radd

#     def __radd__(self,other):
#         return other + self.num #6 + 7

# n1 = Number(6)
# n2 = Number(7)
# print(n1 + n2)


from pyrsistent import s


def get_gcd(a, b):
    for i in range(min(abs(a), abs(b)), 0, -1):
        if a % i == 0 and b % i == 0:
            return -i if a < 0 and b < 0 else i
    return b


def get_frac(object):
    if isinstance(object, Fraction):
        return object
    elif isinstance(object, int):
        return Fraction(object, 1)
    elif isinstance(object, float):
        b = 10**len(str(object).split('.'))
        return Fraction(int(object*b), b)


class Fraction:

    def __init__(self, a, b):
        gcd = get_gcd(a, b)
        self.a = a // gcd
        self.b = b // gcd

    def __str__(self):
        if self.a == 0:
            return "0"
        if self.b == 1:
            return f"{self.a}"
        if self.b == -1:
            return f"{-self.a}"
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        other = get_frac(other)
        return Fraction(self.a*other.b+other.a*self.b, self.b*other.b)

    def __sub__(self, other):
        other = get_frac(other)
        return Fraction(self.a*other.b-other.a*self.b, self.b*other.b)

    def __mul__(self, other):
        other = get_frac(other)
        return Fraction(self.a*other.a, self.b*other.b)

    def __truediv__(self, other):
        other = get_frac(other)
        return Fraction(self.a*other.b, self.b*other.a)

    def __radd__(self, other):
        other = get_frac(other)
        return Fraction(other.a*self.b+other.b*self.a, other.b*self.b)
    
    def __rsub__(self, other):
        other = get_frac(other)
        return Fraction(other.a*self.b-other.b*self.a, other.b*self.b)
    
    def __rmul__(self,other):
        other = get_frac(other)
        return Fraction(other.a*self.a,other.b*self.b)
    
    def __rtruediv__(self, other):
        other = get_frac(other)
        return Fraction(other.a*self.b,other.b*self.a)

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
# print(f1)
# print(f2)
# print(f1+f2)
# print(f1-f2)
# print(f1*f2)
# print(f1/f2)
# print(f1+4.2)
print(4+f1)
print(4-f1)
print(4*f1)
print(4/f1)
print(0*f1)