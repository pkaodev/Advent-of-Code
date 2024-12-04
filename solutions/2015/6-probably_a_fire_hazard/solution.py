import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    data = data[0] if len(data) == 1 else data
    
def make_instructions(data):
    instructions = []
    for line in data:
        _ = line.split(' ')
        if len(_) == 5:
            instructions.append(
                (_[1], _[2].split(','), _[4].split(','))
            )
        else:
            instructions.append(
                (_[0], _[1].split(','), _[3].split(','))
            )
    return instructions
    
instructions = make_instructions(data)

grid = [
   [ False for x in range(1000)]
   for y in range(1000)
]
def q1_1():
    for instruction in instructions:
        for x in range(int(instruction[1][0]), int(instruction[2][0])+1):
            for y in range(int(instruction[1][1]), int(instruction[2][1])+1):
                if instruction[0] == 'off':
                    grid[x][y] = False
                if instruction[0] == 'on':
                    grid[x][y] = True
                if instruction[0] == 'toggle':
                    grid[x][y] = not grid[x][y]
                    
    solution = 0
    for y in range(1000):
        for x in range(1000):
            solution += 1 if grid[x][y] == True else 0
            
    return solution

def q2_1():
    for instruction in instructions:
        for x in range(int(instruction[1][0]), int(instruction[2][0])+1):
            for y in range(int(instruction[1][1]), int(instruction[2][1])+1):
                if instruction[0] == 'off':
                    grid[x][y] -= 1 if grid[x][y] > 0 else 0
                if instruction[0] == 'on':
                    grid[x][y] += 1
                if instruction[0] == 'toggle':
                    grid[x][y] += 2
        
    solution = 0
    for y in range(1000):
        for x in range(1000):
            solution += grid[x][y]
            
    return solution

print(solution)