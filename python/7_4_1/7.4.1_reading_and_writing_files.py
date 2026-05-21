with open('file.txt') as file: # `with` function which uses the file handler, where the var is `file` and the value is the returned file handler object
    content = file.read() # using our `file object, we make use of read() method on it to read all contents, setting that as a value
    print(content)


'''
in other cases you might consider using close() method to close the file, this would clear the handler from memory to avoid it lingering, in this case we are doing a block scoped approach
'''


with open('newFile.txt', 'w') as file:
    file.write("Hello, I'm some text inside a file.")
