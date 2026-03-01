#TASK 4
# 1 odd amd even list segretion
from http.cookiejar import uppercase_escaped_char
from itertools import count
from operator import countOf
from plistlib import InvalidFileException

# pythonList = [10,501,22,37,100,999,87,351]
"""even = []
odd = []
for i in pythonList:
    if i % 2 == 0:
        even.append(i)

    else:
        odd.append(i)

print(f'The even list is {even}, The odd list is {odd}')"""

#2 Prime numbers and make a pyhton list
"""prime=[]
for i in pythonList:
    isprime = True
    for j in range(2,i):

        if i % j == 0:
            isprime = False
            break

    if isprime:
        prime.append(i)



print(f'The prime list is {prime}')"""

#Sum of first and last digit of an integer

# (i) For list
"""after_sum=[]
for i in range(len(pythonList)):
    number_to_string = pythonList[i]
    numm = str(number_to_string)
    separated_values=[]
    for i in numm:
        k = int(i)
        separated_values.append(k)
    after_sum.append(separated_values[0]+separated_values[len(separated_values)-1])

print(f"After the addition of first and last digit of a number {after_sum} ")

# (ii) For single integer

g = [201]
separated_values = []
number_to_string = g[0]
numm = str(number_to_string)
for i in numm:
    k = int(i)
    separated_values.append(k)
print(separated_values[0]+separated_values[len(separated_values)-1])
"""
















# vowels check
# string= input("enter a string:").upper()
# count=0
# for i in string:
#     if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
#         print(i)
#         count +=1
# print(f"the count of vowels  {count}")












