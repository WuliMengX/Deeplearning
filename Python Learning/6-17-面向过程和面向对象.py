class Student(object):  #通常自定义的类首字母要大写
                        #所有类都默认继承object类，是所有类的基类（父类），Student为子类
    def __init__(self, name, age, adres): #实例变量 初始化方法会自动调用
        self.names = name
        self.ages = age
        self.addres = adres
        
    def eat(self):  #self表示当前调用的实例对象
        print(f"{self.names}吃菜")
        print(f"{self.names}扒饭")
    
    @classmethod #类方法的装饰器    
    def sleep(cls): #cls表示当前调用的类对象
        print(cls)
        print(f"今天在{cls.school}上了一天的课，想睡觉了")
    
    @staticmethod #静态方法修饰器
    def eat(): 
        print("我要开动了")
        
    school = "深兰交大"  #类变量
        
stu1 = Student("张三",18,"威宁路")
stu2 = Student("李四",19,"长宁路")
# print(stu1.names)
# print(stu1.ages)
# print(stu1.addres)
# print(stu2.names)
# print(stu2.ages)
# print(stu2.addres)
# print(Student.school)
# print(stu1.school)
# print(stu2.school)




"""
    构造方法（魔术方法）
    调用__new__(cls)把类名传给cls，构造出一个实例对象
    实例对象会由__init__(self)进行定属性，然后由__new__返回，所以__init__不能有返回值，即返回None
    
    __new__（构造方法）和__init__（初始化方法）是协同关系，也可以说都是初始化方法
    
    类里面的叫做方法，不在类里面的叫做函数
    参数带self的是对象方法，参数带cls的是类方法，函数可以没有参数
    self cls不是关键字，可以自定义，但要作为第一个参数
    
"""

""" 实例变量 是每个实例对象独有的，只能由实例对象调用
    类变量   是每个实例对象共有的，实例对象也能调用，但推荐用类调用
    
    实例对象优先调用变量名相同的实例变量，而不是类变量
"""

""" 动态定义实例变量 变量存在则修改，不存在则定义新变量"""
# stu1.height = 178
# print(stu1.height)
# stu1.ages = 38
# print(stu1.ages)

""" 动态定义类变量 变量存在则修改，不存在则定义新变量"""
# Student.school = "交大深兰"
# print(Student.school)

""" 对象方法调用只能用实例对象调用 """
# stu1.eat()
# stu2.eat()

""" 实例属性只能由实例对象调用 """

""" 类方法调用 推荐用类调用，实例对象也能调用 """
# Student.sleep()
# stu1.sleep()

""" 静态方法调用 推荐用类调用，实例对象也能调用"""
# Student.eat()
# stu1.eat()

"""
    静态方法和类方法的区别：
"""

""" 与属性操作相关的内置函数 """
"""
    delattr(object,name) 删除类属性或实例属性name   #del Object.name
    
    getattr(object,name[,default])  返回object对象的name属性值 等价于object.name
                                    如果name属性不存在，且提供了default值，则返回它，否则出发AttributeError
                                    
    hasattr(object,name)    判断object对象是否包含name属性，返回True或False
                            此功能是通过调用getattr(object,name)看是否有AttributeError异常来实现的
                            
    setattr(object,name,value)  将object的name属性设置为value，属性不存在则新增属性                          
                                                              
"""

"""面向对象的三大特性"""
"""
    封装：
        在属性或者方法前面加两个下划线开头，声明为私有属性或者私有方法
        私有属性或者私有方法只能在类的内部调用, 不能在类的外部直接调用
        但是可以提供公有方法来访问私有属性, 或者调用私有方法
        子类无法继承父类的私有属性和私有方法
        
    继承：
        所有的类都默认继承 object，只是一般不用写出来
        子类继承父类后，会拥有父类中所有的非私有属性和方法
        继承的作用：从子类来看，继承可以简化代码；从父类来看，子类是对父类功能的扩充
        
        单继承：继承父类个数为一个
        
        多重继承：继承父类为多个
        
        
        
"""