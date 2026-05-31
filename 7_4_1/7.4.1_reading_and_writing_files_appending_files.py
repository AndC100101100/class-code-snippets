with open('file.txt') as file: 
    content = file.read()
    print(content)

print('---')

with open('file.txt', 'a') as file:
    file.write("fessional.")


with open('file.txt') as file: 
    content = file.read()
    print(content)

'''
Python doesn't add what you provide on the next line or think about formatting for you it simply  appends it at the end of the file. append mode will move the file pointer on our drive to the start of the file, establish the lenght of it and then move the pointer to the end
so, when we begin to write, that is where our string will be added,
where the file pointer is
'''

