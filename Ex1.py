# Write a Python program to print the following
# string in a specific format
# http://www.w3resource.com/python-exercises/python-basic-exercises.php#EDITOR
chorus = 'Twinkle, twinkle, little star,'
chorus2 = 'How I wonder what you are'

# struggled with \t
# Mistake: wanting to attach '\t' within chorus2
# Remember +
print (chorus)
print ('\t'+chorus2 + '!')
# finding an alternative to \t\t
# most efficient, debatable.
print ('\t'*2 + 'Up above the world so high,')
print ('\t\t' + 'Like a diamond in the sky.')
print (chorus)
print ('\t'+chorus2)

# Alternative:
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high,
# \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# Early stages of my Python programming
# Distinguishing which is more "Pythonic'




