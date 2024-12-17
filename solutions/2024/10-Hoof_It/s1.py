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
    data = file.read().split("\n")
    
    _data = []
    
    for row in data:
        _row = []
        for space in row:
            _row.append(int(space))
        _data.append(_row)
        
    data = _data
    
    print(data)

def solution_1(data):
    """
    for each peak (9) find which trailhead (0) can be reached legally
    """
    x_max = len(data[0]) - 1
    y_max = len(data) - 1
    
    def find_trailheads(x, y, trailheads=None):
        if trailheads is None:
            trailheads = set()
        
        next_val = data[y][x] - 1
        
        if x > 0 and data[y][x-1] == next_val:
            if next_val == 0:
                trailheads.add((x-1, y))
            else:
                find_trailheads(x-1, y, trailheads)
                
        if x < x_max and data[y][x+1] == next_val:
            if next_val == 0:
                trailheads.add((x+1, y))
            else:
                find_trailheads(x+1, y, trailheads)
                
        if y > 0 and data[y-1][x] == next_val:
            if next_val == 0:
                trailheads.add((x, y-1))
            else:
                find_trailheads(x, y-1, trailheads)
            
        if y < y_max and data[y+1][x] == next_val:
            if next_val == 0:
                trailheads.add((x, y+1))
            else:
                find_trailheads(x, y+1, trailheads)
                
        return trailheads
            
            
    
    trailheads = {}
    
    for x in range(x_max + 1):
        for y in range(y_max + 1):
           
           if data[y][x] == 9:
               _trailheads = find_trailheads(x, y)
               
               
               for trailhead in _trailheads:
                    if trailhead not in trailheads:
                       trailheads[trailhead] = 1
                    else:
                        trailheads[trailhead] += 1
                        
    solution = sum(trailheads.values())
    print(solution)
               
    
    
    

def solution_2(data):
    """
    for each peak (9) find each unique path that leads to a trailhead (0)
    """
    x_max = len(data[0]) - 1
    y_max = len(data) - 1
    
    def find_trails(x, y):
        trails = 0
        next_val = data[y][x] - 1
        
        if x > 0 and data[y][x-1] == next_val:
            if next_val == 0:
                trails += 1
            else:
                trails += find_trails(x-1, y)
                
        if x < x_max and data[y][x+1] == next_val:
            if next_val == 0:
                trails += 1
            else:
                trails += find_trails(x+1, y)
                
        if y > 0 and data[y-1][x] == next_val:
            if next_val == 0:
                trails += 1
            else:
                trails += find_trails(x, y-1)
            
        if y < y_max and data[y+1][x] == next_val:
            if next_val == 0:
                trails += 1
            else:
                trails += find_trails(x, y+1)
                
        return trails
    
    num_trails = 0
    
    for x in range(x_max + 1):
        for y in range(y_max + 1):
           
           if data[y][x] == 9:
               peak_trails = find_trails(x, y)
               print(peak_trails)
               num_trails += peak_trails
               

    print(num_trails)

if __name__ == "__main__":
    # solution_1(data)
    solution_2(data)
