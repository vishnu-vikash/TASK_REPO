

def addition(x):
    print(f"This is from addition function where value of x is {x}")
    def wrapper(y):
        return x + y
    print(wrapper(20) )

print(addition(5))
