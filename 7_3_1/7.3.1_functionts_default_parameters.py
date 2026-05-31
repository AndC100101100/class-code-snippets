'''
if we wanted to have a parameter that receives is set 
with a default value in case it does not receive an 
argument when being called, we set that parameter
as the last
'''

def greet_user(title, name, greeting='Hello'):
    print('%s %s %s!' % (greeting, title, name))

greet_user(name='Andres', greeting='Hi', title='Mr')
greet_user(name='Carla', title='Mrs') # using keyword arguments were we reference the actual name of the parameter we are passing our value to

