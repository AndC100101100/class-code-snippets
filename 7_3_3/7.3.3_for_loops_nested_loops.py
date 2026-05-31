grid_width = 24
grid_height = 12

blocks = [[8,3],[17,3],[8,4],[17,4],[8,5],[17,5],[5,7],[20,7],[5,8],[20,8],[6,9],[7,9],[18,9],[19,9],[8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[14,10],[15,10],[16,10],[17,10]]

output = ""

for y in range(1, grid_height + 1):
    for x in range(1, grid_width + 1):
        char = "."
        for data in blocks: 
            if (x == data[0] and y == data[1]):
                char = "#"
        output += char
    output += "\n"

print(output)
