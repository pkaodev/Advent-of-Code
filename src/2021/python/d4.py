import copy

bingo_list = []

with open("d4input", "r") as input:
    number_string = input.readline()
    drawn_numbers = [i for i in number_string.split(',')]
    for k in range(100):
        grid_list = []
        input.readline()
        for l in range(5):
            grid_list.append(input.readline().strip('\n').split(' '))
        bingo_list.append(grid_list)

bingo_list2 = copy.deepcopy(bingo_list)

print(bingo_list2)
print(drawn_numbers)
print(bingo_list)
print(len(bingo_list))
print(len(bingo_list[0]))
print(len(bingo_list[0][0]))
print(bingo_list[0][0][1])

for n in drawn_numbers:
    for o in range(len(bingo_list)):
        for p in range(5):
            for q in range(5):
                if bingo_list[o][p][q] == n:
                    bingo_list[o][p][q] = 'X'
                    for r in range(len(bingo_list)):
                        for s in range(5):
                                #row
                                if bingo_list[r][s][0] == bingo_list[r][s][1] ==bingo_list[r][s][2] ==bingo_list[r][s][3] ==bingo_list[r][s][4] == 'X':
                                    print('Winner')
                                    print(int(n) * (int(bingo_list2[r][s][0]) + int(bingo_list2[r][s][1]) + int(bingo_list2[r][s][2]) + int(bingo_list2[r][s][3]) + int(bingo_list2[r][s][4])))
                                    break
                                #column
                                elif bingo_list[r][0][s] == bingo_list[r][1][s] ==bingo_list[r][2][s] ==bingo_list[r][3][s] ==bingo_list[r][4][s] == 'X':
                                    print('Winner')
                                    print(int(n) * (int(bingo_list2[r][1][s]) + int(bingo_list2[r][2][s]) + int(bingo_list2[r][3][s]) + int(bingo_list2[r][4][s]) + int(bingo_list2[r][s][0])))
                                    break
                                #positive diag
                                elif bingo_list[r][4][0] == bingo_list[r][3][1] ==bingo_list[r][2][2] ==bingo_list[r][1][3] ==bingo_list[r][0][4] == 'X':
                                    print('Winner')
                                    print(int(n) * (int(bingo_list2[r][4][0]) + int(bingo_list2[r][3][1]) + int(bingo_list2[r][2][2]) + int(bingo_list2[r][1][3]) + int(bingo_list2[r][0][4])))
                                #negative diag
                                elif bingo_list[r][0][0] == bingo_list[r][1][1] ==bingo_list[r][2][2] ==bingo_list[r][3][3] ==bingo_list[r][4][4] == 'X':
                                    print('Winner')
                                    print(int(n) * (int(bingo_list2[r][0][0]) + int(bingo_list2[r][1][1]) + int(bingo_list2[r][2][2]) + int(bingo_list2[r][3][3]) + int(bingo_list2[r][4][4])))
                                else:
                                    pass









                    #winner
print('end')