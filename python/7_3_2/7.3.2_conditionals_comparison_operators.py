pet = 'dog'

'''
worth mentioning that when we are comparing strings
we are comparing the numerical values of their 
unicode/ascii denary value, using ord() is a good 
way to analyze it
'''

print('dog' == 'dog')  # True
print('dog' == 'DOG')  # False
print(pet == 'dog')    # True
print('dog' == 'cat')  # False
print('dog' != 'cat')  # True
print(123 != 99)       # True
print(123 > 99)        # True
print('dog' > 'cat')   # True
print('dog' < 'cat')   # False
print(123 >= 123)      # True
print('dog' <= 'cat')  # False
print('dog' >= 'cat')  # True

'''
Equal to ==
Not equal to !=
Less than <
Greater than >
Less than or equal to <=
Greater than or equal to >=
'''
