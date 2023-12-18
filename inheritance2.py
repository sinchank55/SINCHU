class A:
    def show(self):
        print("i am in base class 1")

class B:
    def show(self):
        print("i am in base class 2")

class C(A,B):
    pass

obj=C()
obj.show()