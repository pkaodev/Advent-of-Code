import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.join(current_dir, "../../../templates/python")
sys.path.append(utils_path)
import utils

# input_file = "input_example"
input_file = "input"

input_path = os.path.join(current_dir, input_file)


def solution_1():
    # (x, y) coordinate tuples
    rolls = []

    with open(input_path, "r", encoding="utf8") as file:
        x = -1
        for line in file:
            x += 1
            y = -1
            for char in line:
                y += 1
                if char == "@":
                    rolls.append((x, y))

    # 8-neighbour coordinate offsets
    offsets = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

    result = 0


    for roll in rolls:
        num_neighbours = 0
        for offset in offsets:
            rx, ry = roll
            dx, dy = offset
            if (rx+dx, ry+dy) in rolls:
                num_neighbours += 1
            
        if num_neighbours < 4:
            result += 1





    print(result)

def solution_2():
    """
    1a - find/count rolls that can be removed += result
    1b - pop removed from `rolls` *AFTER* all have been removed
    ...
    repeat 
    """
    # (x, y) coordinate tuples
    rolls = set()

    with open(input_path, "r", encoding="utf8") as file:
        x = -1
        for line in file:
            x += 1
            y = -1
            for char in line:
                y += 1
                if char == "@":
                    rolls.add((x, y))

    # 8-neighbour coordinate offsets
    offsets = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

    result = 0

    # also (x, y) coord
    rolls_to_remove = set()

    while True:
        for roll in rolls:
            num_neighbours = 0
            for offset in offsets:
                rx, ry = roll
                dx, dy = offset
                if (rx+dx, ry+dy) in rolls:
                    num_neighbours += 1
                
            if num_neighbours < 4:
                result += 1
                rolls_to_remove.add(roll)

        if not rolls_to_remove:
            break

        rolls = {roll for roll in rolls if roll not in rolls_to_remove}
        rolls_to_remove = set()

    print(result)

if __name__ == "__main__":
    # solution_1()
    solution_2()