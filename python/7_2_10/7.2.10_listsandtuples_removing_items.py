'''
remove adds better control by allowing us to directly reference 
the name of the item we want to remove 
'''
travel_bucket_list = ['Tokyo', 'Hawaii', 'London']
travel_bucket_list.remove('Hawaii')

print(travel_bucket_list) # Tokyo and London


'''
we can also just remove whatever it is that we 
have at the end of a list by using the pop() method
'''
travel_bucket_list.pop()

print(travel_bucket_list) # Tokyo

