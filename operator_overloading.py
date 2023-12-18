from abc import ABC,abstractmethod
class A:
    @abstractmethod
    def method(self,y):
        pass

class B(A):
    def method(self,y):
        print(y*y)

class C(A):
    def method(self,y):
        print(y*2)

class D(A):
    def method(self,y):
        print(y+2)

obj=B()
obj1=C()
obj2=D()

obj.method(10)
obj1.method(2)
obj2.method(3)

