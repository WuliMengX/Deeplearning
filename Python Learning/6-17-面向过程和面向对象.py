class Student(object):  #通常自定义的类首字母要大写
                        #所有类都默认继承object类，是所有类的基类（父类），Student为子类
    def __init__(self, name, age, adres): #实例变量
        self.names = name
        self.ages = age
        self.addres = adres
        
    school = "深兰交大"  #类变量
    
    def eat(self):
        print(f"{self.names}吃菜")
        print(f"{self.names}扒饭")
    
    @classmethod #类方法的装饰器    
    def sleep(cls):
        print("我睡觉了")
    
    @staticmethod #静态方法修饰器
    def eat(): 
        print("我要开动了")
        
        
        
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
    
    实例变量是每个实例对象独有的，只能由实例对象调用
    类变量是每个实例对象共有的,实例对象也能调用，但推荐用类调用
    
    类里面的叫做方法，不在类里面的叫做函数
    参数带self的是对象方法，参数带cls的是类方法，函数可以没有参数
    
    
"""

""" 动态定义实例变量 变量存在则修改，不存在则定义新变量"""
# stu1.height = 178
# print(stu1.height)
# stu1.ages = 38
# print(stu1.ages)

""" 动态定义类变量 变量存在则修改，不存在则定义新变量"""
# Student.school = "交大深兰"
# print(Student.school)

""" 对象方法调用 """
stu1.eat()
stu2.eat()
Student.eat(stu1)