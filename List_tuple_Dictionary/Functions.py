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

def finsPassOrfail(mark):
    if(mark > 35):
        print("PASS")

    else:
        print("fail")
a=int(input("enter first number :"))
finsPassOrfail(a)

def printRange(a,b):
    for i in range(a, b):
        print(i)
a= int(input("enter first number :"))
b= int(input("enter second number :"))
printRange(a,b)
