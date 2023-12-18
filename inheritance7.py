class A:
    def func(self):
        print("sinchan")
class B:
    def func(self):
        print("karmakar")
    def ano(self):
        print("i am in class B but in different method")


obj1=A()
obj2=B()
obj1.func()
obj2.func()
obj2.ano()