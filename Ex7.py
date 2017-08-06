# Write a Python program to accept a filename from the user and
# print the extension of that.

# Trial 1: the condition statement would not print
i = (input('Enter filename: '))
# Attempt: if i contain the substring ".java" --> print Java
# if i == '.java'
# instead use endswith()
if i.endswith('.java'):
    print ('Java')
elif i.endswith('.py'):
    print ('Python')
else:
    print ('Other')

# Learn to implement split()
# Sample sol:
# filename = input("Input the Filename: ")
## f_extns = filename.split(".")
## print ("The extension of the file is : " + repr(f_extns[-1]))
