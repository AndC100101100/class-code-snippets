lunch_stats = {'month': 'June', 'choices': {'sandwich': 21, 'pizza': 37, 'soup': 8}}

print('Month: ' + str(lunch_stats['month']))
print('Lunch items: ')
print('- ' + str(lunch_stats['choices']))
print('Most popular lunch item in June: ')
'''
getting the most popular lunch from our next dictionary
choices. WE consider the maximum value from lunch_stats[choices]
getting the value as the possibilities to consider when 
establishing the highest value. most_popular will retrieve the key
for the object with higher int value in this case, pizza
'''
most_popular = max(lunch_stats['choices'], key=lunch_stats['choices'].get)
print('- ' + most_popular)
