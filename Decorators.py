"Python decorator gives us the ability to add new behavior to the given objects dynamically."
"In the example below, we’ve written a simple example to display a message pre and post the execution of a function."

def decorator_sample(func):
    def decorator_hook(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return decorator_hook

@decorator_sample
def product(x, y):
    "Function to multiply two numbers."
    return x * y

@decorator_sample
def product2(x,y,z):
    return x * y * z

print(product(3, 3))
print(product2(3, 4, 5))
"The output is:"

"Before the function call"
"After the function call"
"9"