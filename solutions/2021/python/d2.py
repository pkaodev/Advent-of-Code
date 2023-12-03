#floaty boat
x_coord = 0
y_coord = 0
aim = 0

#make a list from input file
parsed_list = []
with open('d2input') as j:
    parsed_list = j.readlines()

#do the things from the list
for i in parsed_list:
    if 'forward' in i:
        x_coord += int(i[8:])
        y_coord += int(i[8:]) * aim
    elif 'down' in i:
        #y_coord += int(i[5:])
        aim += int(i[5:])
    elif 'up' in i:
        #y_coord -= int(i[3:])
        aim -= int(i[3:])

#get the answer
final_value = x_coord * y_coord
print(final_value)
