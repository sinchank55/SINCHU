try:
    x = int(input("Enter any number from 1 to 10 "))
    assert x >= 5 and x <= 10, ("The number entered is ", x)

except AssertionError as j:
    print("condition failed")
    print(j)
    