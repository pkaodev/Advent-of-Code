import copy

with open('d13input', 'r') as input_file:
    input_list = [line.rstrip('\n') for line in input_file]


dot_list = []
fold_list = []
for i in input_list:
    if i == '':
        pass
    elif i[0] == 'f':
        fold_list.append(i)
    else:
        dot_list.append(i.split(','))
for i in range(2):
    for j in range(len(dot_list)):
        dot_list[j][i] = int(dot_list[j][i])
print(dot_list)
x_list = [i[0] for i in dot_list]
y_list = [i[1] for i in dot_list]
print(fold_list)

row = [0 for i in range(max(x_list)+1)]
map = [copy.deepcopy(row) for i in range(max(y_list)+1)]


def print_map(mappy):
    for i in mappy:
        print(i)
    print()

for coord in dot_list:
    map[coord[1]][coord[0]] = 1

print_map(map)

for instruction in fold_list:
    #vert left
    if instruction[11] == 'x':
        new_row = [0 for i in range(int(instruction[13:]))]
        new_map = [copy.deepcopy(new_row) for i in range(len(map))]
        print_map(new_map)
        print('hi')
        for x in range (int(instruction[13:])):
            for y in range (len(map)):
                if (map[y][x] == 1) or (map[y][-x-1] == 1):
                    new_map[y][x] = 1
        map = new_map
        print_map(map)
        print()


    #horz up
    elif instruction[11] == 'y':
        new_row = [0 for i in range(len(map[0]))]
        new_map = [copy.deepcopy(new_row) for i in range(int(instruction[13:]))]
        print_map(new_map)
        for x in range(len(map[0])):
            for y in range(int(instruction[13:])):
                if (map[y][x] == 1) or (map[-y-1][x] == 1):
                    new_map[y][x] = 1
    map = new_map
    print_map(map)
    print()
print()




counter = 0
for i in map:
    for j in i:
        if j == 1:
            counter +=1

print(counter
      )