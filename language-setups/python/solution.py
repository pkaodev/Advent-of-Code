import os
input_path = os.path.join(os.path.dirname(__file__), 'input_example')
with open(input_path, 'r', encoding='utf8') as file:
    data = file.read()
lines = data.split('\n')





SOLUTION_1 = None

print(f"SOLUTION_1: {SOLUTION_1}")