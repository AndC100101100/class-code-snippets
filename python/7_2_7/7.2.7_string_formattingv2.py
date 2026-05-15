'''
using format() method, allows for more control
referring to them by their order in the list
'''
first_name = "James"
last_name = "Bond"
print("The name is {1}, {0} {1}".format(first_name, last_name))

'''
we can also give them variable names instead of referencing their index and or position
'''
first_name = "James"
last_name = "Bond"
print(
  "The name is {last}, {first} {last}"
  .format(first=first_name, last=last_name)
)


print('{:,}'.format(1234567890)) # separating thousands with commas
