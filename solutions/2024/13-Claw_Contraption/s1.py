import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.join(current_dir, '../../../language-setups/python')
sys.path.append(utils_path)
import utils
input_path = os.path.join(os.path.dirname(__file__), 'input_example')
with open(input_path, 'r', encoding='utf8') as file:
    data = file.read()

def parse_input(data):
    lines = data.split('\n')

    # return










SOLUTION_1 = None

print(f"SOLUTION_1: {SOLUTION_1}")
# Example solution: no more than 100 times