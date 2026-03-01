# Write into an empty file
path = 'C:/Users/sanja/PyCharmMiscProject/ Advanced Python/test.txt' # provide path of the file
f = open(file=path, mode='w') # open a file using open(file= file path,mode = mode for file to open)
f.write("This line is written using python") # write something in a file
f.close() # close file

# Reading content from file


# Append newlines in a file
# path = 'C:/Users/sanja/PyCharmMiscProject/List_tuple_Dictionary/test'# provide path of the file
# f = open(file=path, mode='a') # open a file using open(file= file path,mode = mode for file to open)
# f.write("\nThis line is second line using python") # append content in a new line. \n is used for moving cursor to new line.
# f.close() # close file

path = 'C:/Users/sanja/PyCharmMiscProject/ Advanced Python/test.txt'
f = open(file=path, mode='r')
var = f.read()
print(var)