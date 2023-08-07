# Example: zip() function

emp = ["tom", "john", "jerry", "jake"]
age = [32, 28, 33, 44]
dept = ['HR', 'Accounts', 'R&D',"IT"]

# call zip() to map values
out = zip(emp, age, dept)

# convert all values for printing them as set
out = set(out)

# Displaying the final values
print("The output of zip() is : ", end="")
print(out)