# Example
class Test:
    aclass = 'programming'  # A class variable

    def __init__(self, ainst):
        self.ainst = ainst  # An instance variable


# Objects of CSStudent class
test1 = Test(1)
test2 = Test(2)

print(test1.aclass)
print(test2.aclass)
print(test1.ainst)
print(test2.ainst)

# A class variable is also accessible using the class name
print(Test.aclass)

