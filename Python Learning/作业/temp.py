class Biology:
    def sleep(self):
        print("Biology睡觉")
class Animal:
    def sleep(self):
        print("Animal睡觉")
class Cat(Biology):
    def sleep(self):
        print("Cat睡觉")
class Ragdoll(Cat, Animal, Biology):
    def sleep(self):
        super().sleep()  # 调用当前类的父类的sleep方法
        super(Ragdoll, self).sleep()  # 调用Ragdoll类的父类的sleep方法
        super(Animal, self).sleep()  # 调用Animal类的右边那个类的sleep方法
        super(Cat, self).sleep()
        
rd = Ragdoll()
rd.sleep()
