import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.join(current_dir, "../../../templates/python")
sys.path.append(utils_path)
import utils

# input_file = "input_example"
input_file = "input"

input_path = os.path.join(current_dir, input_file)

with open(input_path, "r", encoding="utf8") as file:
    data = file.read().split("\n\n")
    grid = data[0]
    grid = [
        list(row)
        for row in grid.split("\n")
    ]
    instructions = data[1].replace('\n', '')
    print(instructions)

def solution_1():
    max_x = len(grid[0])
    max_y = len(grid)
    directions = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }
    
    def move(xi, yi, dir):
        xn = xi + directions[dir][0]
        yn = yi + directions[dir][1]
        
        if grid[yn][xn] == '.':
            grid[yn][xn] = grid[yi][xi]
            grid[yi][xi] = '.'
            return xn, yn
            
        if grid[yn][xn] == 'O':
            if move(xn, yn, dir) != (xn, yn):
                grid[yn][xn] = grid[yi][xi]
                grid[yi][xi] = '.'
                return xn, yn
            
        return xi, yi
            
    for _x in range(max_x):
        for _y in range(max_y):
            if grid[_y][_x] == "@":
                xr = _x
                yr = _y
                break
            
    for dir in instructions:
        xr, yr = move(xr, yr, dir)
    
    solution = 0
    for _x in range(max_x):
        for _y in range(max_y):
            if grid[_y][_x] == 'O':
                gps_coord = 100 * _y + _x
                solution += gps_coord
    print(solution)
    

def solution_2():
    max_x = len(grid[0])
    max_y = len(grid)
    directions = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }
    
    def move(xi, yi, dir):
        xn = xi + directions[dir][0]
        yn = yi + directions[dir][1]
        
        if grid[yn][xn] == '.':
            grid[yn][xn] = grid[yi][xi]
            grid[yi][xi] = '.'
            return xn, yn
            
        if grid[yn][xn] == 'O':
            if move(xn, yn, dir) != (xn, yn):
                grid[yn][xn] = grid[yi][xi]
                grid[yi][xi] = '.'
                return xn, yn
            
        return xi, yi
            
    for _x in range(max_x):
        for _y in range(max_y):
            if grid[_y][_x] == "@":
                xr = _x
                yr = _y
                break
            
    for dir in instructions:
        xr, yr = move(xr, yr, dir)
    
    solution = 0
    for _x in range(max_x):
        for _y in range(max_y):
            if grid[_y][_x] == 'O':
                gps_coord = 100 * _y + _x
                solution += gps_coord
    print(solution)
    

if __name__ == "__main__":
    # solution_1()
    solution_2()