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
    data = file.read().split(",")

def solution_1(data):
    def is_invalid(num_string):
        """
        True if string has even length and first half == second half
        """
        return (
            len(num_string) % 2 == 0
            and num_string[:int(len(num_string)/2)] == num_string[int(len(num_string)/2):]
            )

    result = 0

    for range_pair in data:
        lower = range_pair.split("-")[0]
        upper = range_pair.split("-")[1]

        for val in range(int(lower), int(upper)+1):
            if is_invalid(str(val)):
                result += val


    print(result)

def solution_2(data):
    def is_invalid(num_string):
        """
        A non-empty string s is composed of repeated smaller substrings if it appears
        as a proper substring of (s + s) with the first and last characters removed.
        """
        return num_string in (num_string + num_string)[1:-1]

    result = 0

    for range_pair in data:
        lower = range_pair.split("-")[0]
        upper = range_pair.split("-")[1]

        for val in range(int(lower), int(upper)+1):
            if is_invalid(str(val)):
                result += val

    print(result)

if __name__ == "__main__":
    solution_1(data)
    solution_2(data)
