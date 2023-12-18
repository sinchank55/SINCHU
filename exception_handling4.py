try:
    x=int(input("Enter any number from 1 to 10 "))
    assert x >=5 and x<=10
    print("The number entered",x)
    
except AssertionError:
    print("The condition has failed")