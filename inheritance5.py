class A:
    def __init__(self,i):
        self.i=i

class B:
    def __init__(self,j):
        self.j=j


class sub(A,B):
    def __init__(self,i,j):
        A.__init__(self,i)
        B.__init__(self,j)
        print("Value of i",self.i)
        print("Value of j",self.j)

obj=sub(2,3)
print(sub.mro())