fav_linux_distros = ['Mint', 'Debian', 'Ubuntu', 'Manjaro', 'Fedora', 'Arch']

print(fav_linux_distros)
#print(fav_linux_distros[0])
#print(fav_linux_distros[1])
#print(fav_linux_distros[2]) 
 

# we can also modify lists, her we are going to change index postion 2 to kali

fav_linux_distros[2] = 'Kali'
print(fav_linux_distros)

# we can also use the sort method

fav_linux_distros.sort()
print(fav_linux_distros)

# and we can reverse it

fav_linux_distros.reverse()
print(fav_linux_distros)

