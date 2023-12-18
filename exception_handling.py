try:
    y=int(input("Enter a number"))
    x=10/y
    print(x)
except ZeroDivisionError:
    print("The number cannot be zero")
except ValueError:
    print("sinchan")