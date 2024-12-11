import os
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input_example')
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    
def solution_1(data):

    # Grid limits
    x_min = 0
    x_max = len(data[0]) - 1
    y_min = 0
    y_max = len(data) - 1
    
    # Positions of antennas, organised by antenna type
    antennas = {}
    for y in range(y_max + 1):
        for x in range (x_max + 1):
            if data[y][x] != ".":
                if data[y][x] not in antennas:
                    antennas[data[y][x]] = []
                antennas[data[y][x]].append((y, x))
        
    # Positions of unique antinodes
    antinodes = set()
    for a_type in antennas:
        for i in range(len(antennas[a_type])):
            for j in range(len(antennas[a_type])):
                
                if j == i:
                    continue
                
                ya, xa = antennas[a_type][i]
                yb, xb = antennas[a_type][j]
                
                y1 = 2*ya - yb
                x1 = 2*xa - xb
                if y1 >= y_min and y1 <= y_max and x1 >= x_min and x1 <= x_max:
                    antinodes.add((y1, x1))
                    
                y2 = 2*yb - ya
                x2 = 2*xb - xa
                if y2 >= y_min and y2 <= y_max and x2 >= x_min and x2 <= x_max:
                    antinodes.add((y2, x2))
          
    # Solution is number of unique antinodes         
    print(len(antinodes))

# solution_1(data)


def solution_2(data):

    # Grid limits
    x_min = 0
    x_max = len(data[0]) - 1
    y_min = 0
    y_max = len(data) - 1
    
    # Positions of antennas, organised by antenna type
    antennas = {}
    for y in range(y_max + 1):
        for x in range (x_max + 1):
            if data[y][x] != ".":
                if data[y][x] not in antennas:
                    antennas[data[y][x]] = []
                antennas[data[y][x]].append((y, x))
        
    # Positions of unique antinodes
    antinodes = set()
    for a_type in antennas:
        for i in range(len(antennas[a_type])):
            for j in range(len(antennas[a_type])):
                
                if j == i:
                    continue
                
                ya, xa = antennas[a_type][i]
                yb, xb = antennas[a_type][j]
                
                y_diff = ya-yb
                x_diff = xa-xb
                
                x = xa
                y = ya
                while y >= y_min and y <= y_max and x >= x_min and x <= x_max:
                    antinodes.add((y,x))
                    y += y_diff
                    x += x_diff
                    
                x = xa
                y = ya
                while y >= y_min and y <= y_max and x >= x_min and x <= x_max:
                    antinodes.add((y,x))
                    y -= y_diff
                    x -= x_diff
                
                # back + forth - do from same antenna (A)
                # can be at each antenna
                
          
    # Solution is number of unique antinodes         
    print(len(antinodes))

solution_2(data)