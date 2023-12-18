class A:
    i=5
    def call(self):
        print("i am in base class")
    @classmethod
    def clas(cls):
        print(cls.i)

class B(A):
    def show(self):
        super().call()
        print("i am in B sub class")

class C(A):
    def show(self):
        print("I am in C subclass")

obj=A()
A.clas()
obj1=B()
obj1.show()