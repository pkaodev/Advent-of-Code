import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    data = data[0] if len(data) == 1 else data
    
list_a = []
list_b = []

for line in data:
    a, b = line.split('   ')
    list_a.append(int(a))
    list_b.append(int(b))

a_sorted = sorted(list_a)
b_sorted = sorted(list_b)

solution_1 = 0

for i in range(len(a_sorted)):
    solution_1 += abs(a_sorted[i] - b_sorted[i])

print(solution_1)

solution_2 = 0
 
a_set = set(a_sorted)
b = 0
b_len = len(b_sorted)

for _a in a_set:
    b = b_sorted.count(_a)
    solution_2 += (_a * b)

print(solution_2)