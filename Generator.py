# Simple Python function
def fn():
    return "Simple Python function."

# Python Generator function
def generate():
    yield "Python Generator function."

#print(next(fn()))
print(next(generate()))

list((var for var in range(10, 20)))
print(list)