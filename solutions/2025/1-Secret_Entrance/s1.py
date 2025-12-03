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

def solution_1(data):
    result = 0
    lock_value = 50
    for turn in data:
        turn_val = int(turn[1:])
        if turn[0] == "R":
            lock_value = (lock_value + turn_val) % 100
        else:
            lock_value = (lock_value - turn_val) % 100
        if lock_value == 0:
            result += 1

    print(result)


def solution_2(data):
    """

    """
    result = 0
    lock_value = 50
    for turn in data:
        turn_val = int(turn[1:])

        if turn[0] == "R":
            for _ in range(turn_val):
                lock_value += 1
                if lock_value == 100:
                    lock_value = 0
                    result += 1

        else:
            for _ in range(turn_val):
                lock_value -= 1
                if lock_value == -1:
                    lock_value = 99
                if lock_value == 0:
                    result += 1

    print(result)



def run_tests():
    pass


if __name__ == "__main__":
    solution_1(data)
    solution_2(data)
