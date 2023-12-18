#for n in range(5):
#    print("sinchan"  )
#print()
#for n in range(10,0,-1):
#    print(n)
i=1
while i<=10:
    print(i,"Welcome to IMA")
    i=i+1
print(i)

w="sinchan"
print(w[4])
print(w[-4])
print(w[0:9])
print(w[0::2])
t=len(w)
print(t)

print(w.find('ch'))

w="welcome {} to {} wscube tech".format("hello",20)
print(w)

l=[10,30,40,50,"hello"]
del l[2]
print(l)
print(l[2],l[3])
print(l[0:2])
print(l[0::2])
print(l[3:])
print(l[-1::-2])
t=len(l)
for n in range(t):
    print(l[n])
for n in range(t-1,-1,-1):
    print(l[n])