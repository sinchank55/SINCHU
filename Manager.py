class Person:
    def __init__(self):
        self.property=9000.00
        self.age=15

    def prop(self):
        print(self.property)
        print(self.age)

class Human(Person):
    def __init__(self):
        self.age=99
        super().__init__(var)
    def prop(self):
        print(self.age)
        super.__init__(var)

h1=human()
h1.prop()