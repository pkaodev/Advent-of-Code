import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.join(current_dir, "../../../templates/python")
sys.path.append(utils_path)
import utils

input_file = "input_example"
# input_file = "input"

input_path = os.path.join(current_dir, input_file)

with open(input_path, "r", encoding="utf8") as file:
    data = file.read().split("\n")

def solution_1(data):
    """
    price = area * perimeter
    """
    print(data)
    x_max = len(data[0]) - 1
    y_max = len(data) - 1
    
    total_cost = 0
    visited = set()
    
    def count_perimeter(x, y):
        plant_type = data[y][x]
        p = 0
        for shift in [(1,0), (-1,0), (0,1), (0,-1)]:
            _x, _y = shift
            _x += x
            _y += y
            if _y < 0 or _y > y_max or _x < 0 or _x > x_max or data[_y][_x] != plant_type:
                p += 1
                continue
        return p
    
    def flood(x, y):
        coord = (x, y)
        if coord in visited:
            return 0, 0
        else:
            visited.add(coord)
            
        area = 1
        perimeter = count_perimeter(x, y)
        
        plant_type = data[y][x]
        
        for shift in [(1,0), (-1,0), (0,1), (0,-1)]:
            _x, _y = shift
            _x += x
            _y += y
            
            if _y < 0 or _y > y_max or _x < 0 or _x > x_max:
                continue
            
            if data[_y][_x] == plant_type:
                _area, _perimeter = flood(_x, _y)
                area += _area
                perimeter += _perimeter
                
        return area, perimeter
    
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if (x, y) in visited:
                continue
            
            area, perimeter = flood(x, y)
            cost = area * perimeter
            total_cost += cost
            
    print(total_cost)

def solution_2(data):
    """
    price = area * num sides
    """
    print(data)
    x_max = len(data[0]) - 1
    y_max = len(data) - 1
    
    total_cost = 0
    visited = set()
    
    def flood(x, y, edge_zones=None):
        coord = (x, y)
        if coord in visited:
            return 0, edge_zones
        else:
            visited.add(coord)
            
        if edge_zones is None:
            edge_zones = set()
            
        area = 1
        plant_type = data[y][x]
        num_similar_neighbors = 0
        
        for shift in [(1,0), (-1,0), (0,1), (0,-1)]:
            _x, _y = shift
            _x += x
            _y += y
            
            if _y < 0 or _y > y_max or _x < 0 or _x > x_max:
                continue
            
            if data[_y][_x] == plant_type:
                num_similar_neighbors += 1
                _area, _edge_zones= flood(_x, _y, edge_zones)
                area += _area
                
        for shift in [(1,1), (-1,1), (1,-1), (-1,-1)]:
            _x, _y = shift
            _x += x
            _y += y
            if _y < 0 or _y > y_max or _x < 0 or _x > x_max:
                continue
            if data[_y][_x] == plant_type:
                num_similar_neighbors += 1
        if num_similar_neighbors != 8:
            edge_zones.add(coord)
        
        return area, edge_zones
    
    def count_sides(edge_zones):
        edges = set()
        
        for x, y in edge_zones:
            for shift in [(1,0), (-1,0), (0,1), (0,-1)]:
                _x, _y = shift
                _x += x
                _y += y
                
                # left
                if _x < 0 or data[_y][_x] != data[y][x]:
                    edges.add((x-0.5, y))
                # right
                if _x > x_max or data[_y][_x] != data[y][x]:
                    edges.add((x+0.5, y))
                # top
                if _y < 0 or data[_y][_x] != data[y][x]:
                    edges.add((x, y-0.5))
                # bottom
                if _y > y_max or data[_y][_x] != data[y][x]:
                    edges.add((x, y+0.5))
        
        return len(edges)
                
    
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            if (x, y) in visited:
                continue
            
            area, edge_zones = flood(x, y)
            sides = count_sides(edge_zones)
            cost = area * sides
            total_cost += cost
            
    print(total_cost)

if __name__ == "__main__":
    # solution_1(data)
    solution_2(data)
