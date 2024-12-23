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
    print(data)

# def solution_2(data):
#     pass

if __name__ == "__main__":
    solution_1(data)
    # solution_2(data)
td