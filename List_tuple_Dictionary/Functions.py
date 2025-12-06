# function is the block of the code which is used to perform a specific task.
# functions are called as methods

def add(a,b):
    print(f"sum is:{a+b}")
a=input("enter first number :")
b=input("enter second number :")
add(int(a),int(b))

def addNumb(a,b):
    print(f"sum is:{a+b}")
x=int(input("enter first number :"))
y=int(input("enter second number :"))
addNumb(10,20)

def addition_of_two_numbers(a,b): # a and b are the arguments / inputs which are passed to a function
    #print(a+b) # printing values/statements on the console
    return a+b
x = int(input("Enter first value to be added: ")) # 10 -> '10' -> int('10') -> 10
# print(type(a))
# a = int(a) # Type conversion -> It is a way to convert data types of a variable
# print(type(a))

y = int(input("Enter second value to be added: "))
z = int(input("Enter third value to be added: "))
print(addition_of_two_numbers(addition_of_two_numbers(x,y),z))

def subtract(a,b):
    print(a-b)
def add(a,b,c):
    result=a+b
    subtract(result,c)
add(20,30,10)

## closure functions

def add(a,b):
    result=(a+b)
    def add2(c):
        print(f"final Output is {result + c}")
    return add2( b)
add(10,5)


