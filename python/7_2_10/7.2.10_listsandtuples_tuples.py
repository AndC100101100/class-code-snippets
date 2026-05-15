'''
tuples are immutable and obligate you to copy data into a new one
so that you can modify data, leaving the original one untouched
'''
coords = (51.1739726374, -1.82237671048)
# coords[0] = 12.3456789 # this line would break our code
print('Stonehenge is at geo position:')
print('%f, %f' % (coords[0], coords[1]))


