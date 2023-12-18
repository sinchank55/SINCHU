from abc import*
class A(object):
    @abstractmethod
    def method(self,i):
        pass
class B(A):
    def method(self,i):
        print(i*i)

obj1=A()
obj2=B()

obj2.method(2)