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
        
        单继承：继承父类个数为一个 父子 父子孙
        
        多重继承：继承父类为多个   多个父类
        
        继承顺序：
                单继承 先找自己，再去找父类，再去好父类的父类等等
                多重继承：先找自己，再去找父类，父类如果有继承，要把继承找完为止，多个父类按照从左往右顺序查找
        
        方法重写：在继承中，当父类的方法功能不能满足需求时，可以在子类重写父类的方法
        
        super([类，self]) 调用指定类的父类（超类）
        适用场景：   a. 在子类重写父类方法后，想再使用父类的该方法   
                    b. 在多重继承时，想要调用指定类的属性或方法     
                    参数中的类如果是调用super的类，则调用该类的父类
                    参数中的类如果是调用super的类的多个父类中的一个，则优先调用这个父类的右边那个类的方法，找不到才调用这个父类的方法    
    
    多态性：
        多态性是指具有不同内容的方法可以使用相同的方法名，则可以用一个方法名调用不同内容的方法
        只要改变相同名字的方法的调用对象，就可以调用不同内容的方法
                      
"""
""" super方法 """
# class Biology:
#     def sleep(self):
#         print("Biology睡觉")
# class Animal:
#     def sleep(self):
#         print("Animal睡觉")
# class Cat(Biology):
#     def sleep(self):
#         print("Cat睡觉")
# class Ragdoll(Cat, Animal, Biology):
#     def sleep(self):
#         super().sleep()               # 调用当前类的父类的sleep方法
#         super(Ragdoll, self).sleep()  # 调用Ragdoll类的父类的sleep方法
#         super(Animal, self).sleep()   # 调用Animal类的右边那个类的sleep方法
#         super(Cat, self).sleep()      # 调用Cat类的右边那个类的sleep方法
        
# rd = Ragdoll()
# rd.sleep()
""" 继承中的__init__方法 """
# class A:
#     def E(self):
#         print('E方法被调用')
#     def __init__(self, name):
#         self.name = name
#         self.Q()
#     def Q(self):
#         print(self.name, 'Q方法被调用')
# class B(A):
#     pass
# b = B('张三')  # 实例化,调用初始化方法,B没有则调用父类中的初始化方法,初始化方法中调用了Q方法
# b.E()  # 调用父类的E方法
# b.Q()  # 调用父类的Q方法
# class C(A):
#     def __init__(self, name):
#         self.names = name
# c = C('赵六')  # 实例化, 优先调用C中初始化方法
# """
# 虽然可以调用父类的Q方法, 但是因为Q方法中的
# self.name没有定义, 因为A的初始化方法没有被调用, 所以报错
# 解决方案: 先通过c调用一次A的初始化方法 或者 把C类中的
# self.names改为self.name
# """
# # c.Q() # 报错
# class D(A):
#     def __init__(self, name):
#         super(D, self).__init__('李四')
#         self.name = name
# d = D('王五')  # 实例化, 先调用D的初始化方法, super方法调用父类的初始化方法, 父类的初始化方法中调用Q方法
# d.Q()  # 调用父类的Q方法

"""  与继承相关的两个内置函数 """
"""
    isinstance(object, classinfo)   object：实例对象
                                    classinfo：类名、基本类型或者由它们组成的元组
                                    如果 object 是 classinfo 的实例或者是其子类的实例，则返回 True
                                    如果 object 不是给定类型的对象，则返回 False
                                    如果 classinfo 是类型对象元组，那么如果 object 是其中任何一个类型的实例或其子类的实例，就返回 True
                                    如果 classinfo 既不是类型，也不是类型元组或类型元组的元组，则将引发 TypeError 异常

    issubclass(class, classinfo)    如果 class 是classinfo 的子类则返回True 
                                    类会被视作其自身的子类
                                    classinfo 也可以是类对象的元组，只要 class 是其中任何一个类型的子类，就返回 True


"""

