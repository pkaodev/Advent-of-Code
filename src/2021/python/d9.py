def aabove():
    if int(input_list[i][j]) < int(input_list[i-1][j]):
        return True
def lleft():
    if int(input_list[i][j]) < int(input_list[i][j-1]):
        return True
def rright():
    if int(input_list[i][j]) < int(input_list[i][j+1]):
        return True
def bbelow():
    if int(input_list[i][j]) < int(input_list[i+1][j]):
        return True


with open('d9input', 'r') as input_file:
        input_list = input_file.read().splitlines()

print('input list[row/y][column/x] is {}'.format(input_list))
risk = 0
#number of rows
for i in range(len(input_list)):
    #number of columns
    for j in range(len(input_list[0])):
        #middle piece
        if ((i > 0) and (i < (len(input_list)-1))) and ((j > 0) and (j < (len(input_list[0])-1))):
            print('middle at {},{}, value {}'.format(i,j,input_list[i][j]))
            if aabove() and lleft() and rright() and bbelow():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])
        #top wall
        if (i == 0) and ((j > 0) and (j < (len(input_list[0])-1))):
            print('top wall at {},{}, value {}'.format(i,j,input_list[i][j]))
            if lleft() and rright() and bbelow():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])

        #left wall
        if ((i > 0) and (i < (len(input_list)-1))) and (j == 0):
            print('left wall at {},{}, value {}'.format(i,j,input_list[i][j]))
            if aabove() and rright() and bbelow():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])

        #right wall
        if ((i > 0) and (i < (len(input_list)-1))) and (j == (len(input_list[0])-1)):
            print('right wall at {},{}, value {}'.format(i,j,input_list[i][j]))
            if aabove() and lleft() and bbelow():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])

        #bottom wall
        if (i == len(input_list)-1) and ((j > 0) and (j < (len(input_list[0])-1))):
            print('bottom wall at {},{}, value {}'.format(i,j,input_list[i][j]))
            if aabove() and lleft() and rright():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])

        #top left corner
        if i == j == 0:
            print('top left corner at {},{}, value {}'.format(i,j,input_list[i][j]))
            if rright() and bbelow():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])

        #top right corner
        if (i == 0) and (j == (len(input_list[0])-1)):
            print('top right corner at {},{}, value {}'.format(i,j,input_list[i][j]))
            if lleft() and bbelow():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])

        #bottom left corner
        if (i == len(input_list)-1) and (j == 0):
            print('bottom left corner at {},{}, value {}'.format(i,j,input_list[i][j]))
            if aabove() and rright():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])

        #bottom right corner
        if (i == len(input_list)-1) and (j == (len(input_list[0])-1)):
            print('bottom right corner at {},{}, value {}'.format(i,j,input_list[i][j]))
            if aabove() and lleft():
                print(input_list[i][j])
                risk += 1 + int(input_list[i][j])



print('risk is {}'.format(risk))




   # print(test_string)
    #print(type(test_string))
   # print(len(test_string))
  #  input_list = [[] for i in range(len(test_string))]
  #  print(input_list)
   # for line in input_file:
     #   print(line)
     #   for j in range(len(test_string)):
    #        input_list[j-1].append(line[j-1])

  #  print(input_list)
