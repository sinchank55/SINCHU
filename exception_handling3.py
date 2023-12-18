class E(Exception):
    def __init__(self,var):
        self.var=var
    def __str__(self):
        return repr(self.var)
try:
    raise E(5)
except E as J:
    print("User defined exception",J.var)
