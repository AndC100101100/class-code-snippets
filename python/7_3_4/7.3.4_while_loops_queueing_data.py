'''
while users checks that users is a list with users in it,
if it is, its truthy and so True. as long as the list has
items it will resolve to true, so we loop. we pop the
item index 0 in the list until the list is empty making
are conditional not met, so falsy and therefore False
'''



users = ['Andres', 'David', 'Cindy', 'Celeste', 'Rachel']


while users: 
    user = users.pop(0)
    print("Hello %s" % users)

print("All Done")
