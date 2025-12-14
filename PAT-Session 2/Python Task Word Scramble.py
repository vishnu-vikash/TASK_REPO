import random
list=["python","javascript","java","automation","pytest","guvi","selenium"]
wordtobescrambled=random.choice(list)
scrambledword=''.join(random.sample(wordtobescrambled,len(wordtobescrambled)))
success=False
print(f"Try to unscramble the given word: {scrambledword}")
for i in range(0,3):
    userInput = input("Enter your choice: ")
    if userInput == wordtobescrambled:
        print(f"Congrats - the scrambled word is {wordtobescrambled}")
        success = True
        break
if success == False:
    print(f"Your times exceeds, The correct word is {wordtobescrambled}")
