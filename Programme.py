#Print as below
#1 12 123 1234 12345
a = 0
while(a<=5):
    a = a + 1
    for i in range(1,a):
        print(str(i), end = "")
    print("",end=" ")

print("\n=====================================")
#1
#12
#123
#1234
#12345
a = 0
while(a<=5):
    a = a + 1
    for i in range(1,a):
        print(str(i), end = "")
    print()
print("\n=====================================")
#*
#**
#***
a = 0
while(a<=3):
    a = a + 1
    for i in range(1,a):
        print("*", end = "")
    print()

print("\n=====================================")
def add_two_numbers(x,y):
    lambda z: x +y
    return z

print(add_two_numbers(5,10))
