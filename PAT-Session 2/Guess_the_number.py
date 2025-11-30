

# Define a range for guessing
# You need to ask for guesing number
# conditional check to validate the guess
# Add re-attempting
from random import randint
randint = randint(0,10)
i=1
while i<=3:
    guess_the_number = input("Enter a number : ")
    g=int(guess_the_number)
    if(g == randint):
        print(f"Congratulations!!!,{g} is correct")
        i+=4

    elif(g>randint):
        print("Too High")
        i+=1


    else:
        print(f"{g} is incorrect, Too Low value")
        i+=1
if(g != randint):
    print(f"The correct number is {randint}")












