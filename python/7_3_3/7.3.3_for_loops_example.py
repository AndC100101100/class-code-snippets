fav_linux_distros = ['Mint', 'Debian', 'Ubuntu', 'Manjaro', 'Fedora', 'Arch']

for distro in fav_linux_distros:
    if (distro == 'Fedora'):
        fav_linux_distros.append('Kali')
        print("...Added Kali")
    print(distro)
