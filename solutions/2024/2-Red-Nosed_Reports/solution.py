import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
	data = file.read().split('\n')
	data = [line for line in data if line.strip()]
    
def score_report_1(report):
    values = list(map(int, report.split()))
    is_increasing = all(b - a in range(1, 4) for a, b in zip(values, values[1:]))
    is_decreasing = all(a - b in range(1, 4) for a, b in zip(values, values[1:]))
    return int(is_increasing or is_decreasing)

def solution_1(data):
    print(sum(score_report_1(report) for report in data))

solution_1(data)

def is_safe(values):
    is_increasing = all(b - a in range(1, 4) for a, b in zip(values, values[1:]))
    is_decreasing = all(a - b in range(1, 4) for a, b in zip(values, values[1:]))
    return is_increasing or is_decreasing

def score_report_2(report):
    values = list(map(int, report.split()))
    if is_safe(values):
        return 1
    for i in range(len(values)):
        other_values = values[:i] + values[i+1:]
        if is_safe(other_values):
            return 1
    return 0

def solution_2(data):
    print(sum(score_report_2(report) for report in data))
    
solution_2(data)