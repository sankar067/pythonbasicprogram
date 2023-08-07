alist = ["apple","mango","orange"]
astr = "banana"

list_obj  = enumerate(alist)
str_obj = enumerate(astr)

print("list_object type:", type(list_obj))
print("str_obj type:", type(str_obj))

print(list(enumerate(alist)) )
# Move the starting index to two from zero
print(list(enumerate(astr, 2)))