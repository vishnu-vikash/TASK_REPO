vishnu_dream = ["School","College","Work","School1","College2","Work3"]
print(len(vishnu_dream)) #lenght of the given list
print(vishnu_dream[0],vishnu_dream[1])  # this [0] will show the value in the list position
print(vishnu_dream[0]+vishnu_dream[1])
print(vishnu_dream)

#for fethching anf prininting each item at a time using indesxing

for i in range(len(vishnu_dream)):
    print(f"this is printing {vishnu_dream[i]}")

for i in range(2):
    print(vishnu_dream[i])

vishnu_dream.insert(5,"Vishnu") # insert a value in the specific index

print(vishnu_dream)
vishnu_dream.append("VishnuVikash") # insert a value at the end of the list

print(vishnu_dream)
vishnu_dream.pop() # This will pop the last index if index value is not provided
print(vishnu_dream)
vishnu_dream.pop(4) # This will pop the  index  value 
print(f"{vishnu_dream} This pop the value at index 4")
