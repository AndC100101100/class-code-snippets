'''
we take every character in the text, convert it to the character 
reference using ord() and then format that decimal to binary,
joining the resultig binary values with the spaces between
'''
text = "hello world"
binary = ' '.join(format(ord(char), 'b') for char in text)
print(binary)
