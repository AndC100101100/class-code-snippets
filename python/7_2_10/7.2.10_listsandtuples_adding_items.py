travel_bucket_list = ['Tokyo', 'Hawaii', 'London']
travel_bucket_list.append('New York')
travel_bucket_list.append(['Berlin', 'Helsinki', 'Managua'])
print(travel_bucket_list)

'''
to have better control of the index were we want to insert the 
data we desire, we can use the insert() method which receives
the index position and the item to inser
'''
travel_bucket_list.insert(1, 'San Jose') # appending San Jose to the second position
print(travel_bucket_list)
