class Employee
    def Setname(self,name):
        self.name=name
    def getname(self):
        return self.name

class Manager(Employee):
    def SetSalary(self,salary):
        self.salary=salary
    def getsalary(self):
        return self.salary

