import os
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input_example')
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    
def solution_1(data):
    data = [list(_) for _ in data]
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                xg = j
                yg = i
                break
            
    x_min = 0
    x_max = len(data[0])
    y_min = 0
    y_max = len(data)
            
    dirs = [
        {"x": 0, "y": -1},
        {"x": 1, "y": 0},
        {"x": 0, "y": 1},
        {"x": -1, "y": 0}
    ]
            
    dir_guard_start = 0
    
    while True:
        
        data[yg][xg] = 'X'
        
        xn = xg + dirs[dir_guard_start]["x"]
        yn = yg + dirs[dir_guard_start]["y"]
        
        if xn < x_min or xn >= x_max or yn < y_min or yn >= y_max:
            break
        
        if data[yn][xn] == '#':
            dir_guard_start = (dir_guard_start + 1) % 4
            continue
        
        xg = xn
        yg = yn
        
        
    solution = 0
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'X':
                solution += 1
                
    print(solution)
        
# solution_1(data)


def solution_2(data):
    data = [list(_) for _ in data]
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '^':
                x_guard_start = j
                y_guard_start = i
                break
            
    x_min = 0
    x_max = len(data[0])
    y_min = 0
    y_max = len(data)
            
    dirs = [
        {"x": 0, "y": -1},
        {"x": 1, "y": 0},
        {"x": 0, "y": 1},
        {"x": -1, "y": 0}
    ]    
    dir_guard_start = 0
    
    solution = 0
    
    for yo in range(len(data)):
        for xo in range(len(data[yo])):
            
            if xo == x_guard_start and yo == y_guard_start:
                continue
            if data[yo][xo] == '#':
                continue
            
            new_data = [list(_) for _ in data]
            new_data[yo][xo] = '#'
            
            xg = x_guard_start
            yg = y_guard_start
            dirg = dir_guard_start
            
            prev_moves = set()
            
            while True:
                
                move = f"{xg},{yg},{dirg}"
                if move in prev_moves:
                    solution += 1
                    break
                
                prev_moves.add(move)
                
                xn = xg + dirs[dirg]["x"]
                yn = yg + dirs[dirg]["y"]
                
                if xn < x_min or xn >= x_max or yn < y_min or yn >= y_max:
                    break
                
                if new_data[yn][xn] == '#':
                    dirg = (dirg + 1) % 4
                    continue
        
                xg = xn
                yg = yn
                
    print(solution)
        
solution_2(data)