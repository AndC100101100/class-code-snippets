def show_file_content():
    with open('file.txt', 'r') as file:
        content = file.read()
        print(content)

# Truncate and then write
with open('file.txt', 'w') as file:
    file.write("My really important content")
show_file_content()


# no truncation, read (moved pointer to eof), write
with open('file.txt', 'r+') as file:
    content = file.read()
    file.write("11111")
show_file_content()


# no trucation, write, (but no pointer moved to eof)
with open('file.txt', 'r+') as file:
    file.write("22222")
show_file_content()

# truncate, read (pointer move attempt to EOF, but no bytes)
with open('file.txt', 'w+') as file:
    content = file.read()
    file.write(content + "...got truncated lol")
show_file_content()
