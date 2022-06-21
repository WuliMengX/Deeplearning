class Student(object):  #通常自定义的类首字母要大写
                        #所有类都默认继承object类，是所有类的基类（父类），Student为子类
    def __init__(self, name, age, adres):
        self.names = name
        self.ages = age
        self.addres = adres
        
stu1 = Student("张三",18,"威宁路")
stu2 = Student("李四",19,"长宁路")
print(stu1.names)
print(stu1.ages)
print(stu1.addres)
print(stu2.names)
print(stu2.ages)
print(stu2.addres)

"""
    构造方法（魔术方法）
    调用__new__(cls)把类名传给cls，构造出一个实例对象
    实例对象会由__init__(self)进行定属性，然后由__new__返回，所以__init__不能有返回值，即返回None
    
    __new__（构造方法）和__init__（初始化方法）是协同关系，也可以说都是初始化方法
    
    实例变量是每个实例对象独有的
    
"""

