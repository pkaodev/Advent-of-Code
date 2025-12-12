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
    # 1. ignore full ... rows
    # 2. beams = {x-coord: num_beams} = {S-x: 1} at start
    # 3. get [x1, x2, ... xN] for each splitter row
    # 4. iterate through splitter rows and beams:
    # - make new_beams = {}
    # - where x_beam = y_beam -> new_beams[x-1: +=SAME] and new_beams[x+1: +=SAME] -> RESULT += 1
    # - where no deflection -> new_beams[x: +=SAME ]
    # 5. sum beams.values()
    print(data)

# def solution_2(data):
#     pass

if __name__ == "__main__":
    solution_1(data)
    # solution_2(data)
# P1 example solution: 21