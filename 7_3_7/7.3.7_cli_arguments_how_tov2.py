import sys

projects = ['Aurora', 'Blizzard', 'Cyclone', 'Delta', 'Eagle',  'Frost', 'Ginger', 'Hawk', 'Igloo', 'Jazz', 'Kite', 'Llama', 'Medusa', 'Neptune', 'Orion', 'Plato', 'Quartz', 'Raven', 'Sand', 'Thunder', 'Umbrella', 'Vector', 'Whistle', 'Xorg', 'Yeti', 'Zumba']
length = len(projects)

#print(length)



# we check that the length of the arguments provided ist exactly three, if so, we exit

if len(sys.argv) != 3:
    sys.exit('Program usage is: \npython 7.3.7_cli_arguments_how_to.py <from> <to> \nusing numbers from 0 to ' + str(length))

'''
we know sys.argv returns a list(something like ['output.py', '1', '2']), 
so we reference the item in index 1, the first number set
as an argument and index 2 the second number set as a argument, as the beginning and end
of items we need to iterate through
'''
try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
except:
    sys.exit('Oh Dear')

if start < 0 or end > length or start >= end:
    sys.exit('Sorry, try again with a range between 0 and' + str(length))

print(projects[start:end])

