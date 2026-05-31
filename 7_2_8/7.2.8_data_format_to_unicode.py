memory = "1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100" # hello word
'''
we are splitting the memory data by space characters. this way 
we can have memory chunks and then for each of those chunks,
we can convert it to an integer, which is the character reference
to the convert that into the character
'''

data_chunks = memory.split(' ')

text = ''.join(format(int(chunk, 2), 'c') for chunk in data_chunks)
print(text)

'''
1101000 => 104 => h
1100101 => 101 => e
1101100 => 108 => l
1101100 => 108 => l
1101111 => 111 => o
0100000 => 32  =>
1110111 => 119 => w
1101111 => 111 => o
1110010 => 114 => r
1101100 => 108 => l
1100100 => 100 => d
'''
