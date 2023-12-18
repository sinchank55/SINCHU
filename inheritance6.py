class P(object):
    def show1(self):
        print("I am in class P")

class Q(object):
    def show2(self):
        print("i am in class Q")

class R(object):
    def show3(self):
        print("i am in class R")

class S(Q):
    def show4(self):
        print("i am in class S")

class T(Q):
    def show5(self):
        print("i am in class T")

class U(S,T,R):
    def show6(self):
        print("i am in class U")

obj=U()
obj.show6()
print(U.mro())