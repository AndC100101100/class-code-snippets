tasks_total = 30
tasks_done = 23

tasks_display = "["
current_block= 0

for block in range(1, tasks_total + 1):
    current_block += 1
    if(current_block <= tasks_done):
        tasks_display += "#"
    else: 
        tasks_display += " "

tasks_display += "]"

print("%s : %d of %d" % (tasks_display, tasks_done, tasks_total))
