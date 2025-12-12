import os
import sys
import re

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

    num_rows = len(data)

    _sep_data = [
        re.sub(r" +", ",", line).split(",")
        for line in data
    ]
    print(_sep_data)
    sep_data = []
    for x in range (len(_sep_data)-1):
        new_row = []
        for y in range(len(_sep_data[0])):
            if _sep_data[x][y] != '':
                new_row.append(int(_sep_data[x][y]))
        sep_data.append(new_row)
    sep_data.append(_sep_data[-1])
    print(sep_data)

    result = 0


    for i in range(len(sep_data[0])):
        if sep_data[len(data)-1][0] == "+":
            for j in range(len(data)-1):
                result += int(sep_data[j][i])
        else:
            _sub_result = 1
            for j in range(len(data)-1):
                _sub_result *= int(sep_data[j][i])
            result += _sub_result

    # 6796089
    # 2861975
    print(result)
# def solution_2(data):
#     pass

if __name__ == "__main__":
    solution_1(data)
    # solution_2(data)
# P1 example solution: much