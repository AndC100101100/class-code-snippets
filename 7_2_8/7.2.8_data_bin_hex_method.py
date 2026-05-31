'''
we can use hex() wrapping ord() to convert our values into hexadecimal
hex() converts an integer into its lowercase hexadecimal
string equivalent, always prefixed with 0x
'''
print(hex(ord('A'))) # ord() turns 'A' => 65 and hex() turns 65 => 0x41
print(hex(ord('B'))) # ord() turns 'B' => 66 and hex() turns 66 => 0x42  
print(hex(ord('C'))) # ord() turns 'C' => 67 and hex() turns 67 => 0x43


'''
we can do essentially the same thing and turn our values 
into binary with the use of bin() instead of hex()
'''
print(bin(ord('A'))) # ord() turns 'A' => 65 and bin() turns 65 => 0b1000001
print(bin(ord('B'))) # ord() turns 'B' => 66 and hex() turns 66 => 0b1000010  
print(bin(ord('C'))) # ord() turns 'C' => 67 and hex() turns 67 => 0b1000011

