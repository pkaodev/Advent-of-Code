list_of_instructions = []

with open('d5input', 'r') as input_file:
    for line in input_file:
        csv_string = line.replace(' -> ', ',').replace('\n', '')
        list_of_instructions.append(list(map(int, csv_string.split(','))))

print(list_of_instructions)

map_list = []
column_list = []

for i in range(1000):
    map_list.append([])
    for j in range(1000):
        map_list[i].append(0)

for i in list_of_instructions:
    if i[0] == i[2]:
        if i[1] < i[3]:
            for j in range(i[1], i[3]+1):
                map_list[i[0]][j] += 1
        elif i[3] < i[1]:
            for j in range(i[3], i[1]+1):
                map_list[i[0]][j] += 1
        #horz
    elif i[1] == i[3]:
        if i[0] < i[2]:
            for j in range(i[0], (i[2])+1):
                map_list[j][i[1]] += 1
        elif i[2] < i[0]:
            for j in range(i[2], i[0]+1):
                map_list[j][i[1]] += 1
    #diagonal
    else:
        if i[0] < i[2]



counter = 0
for i in range(1000):
    for j in range(1000):
        if map_list[j][i] >= 2:
            counter += 1
print(counter)

