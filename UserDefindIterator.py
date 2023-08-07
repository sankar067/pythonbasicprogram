class TestIterator():
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            return result
        else:
            raise StopIteration

# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3,5], 4]


# using copy for shallow copy
li2 = copy.copy(li1)

# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)

print(li2)
print(li3)
# Python code to demonstrate copy operations

# Program to double each item in a list using map()

my_list = [1, 5, 'sankar', 6, 8, 11, 3, 12]

#new_list = list(map(lambda x: isinstance(x,str) , my_list))
new_list = list(filter(lambda x: isinstance(x,str) , my_list))
# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
