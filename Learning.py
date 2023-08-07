import re
print('re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"')

str1 = "geek"
print(id(str1))

str2 = "geek"
print(id(str2))

# This will return True
print(id(str1) == id(str2))

# Use in Lists
list1 = ["aakash", "priya", "abdul"]
print(id(list1[0]))
print(id(list1[2]))

# This returns false
print(id(list1[0]) == id(list1[2]))