import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_1_path = os.path.join(os.path.dirname(__file__), 'input1')

with open(input_1_path, 'r', encoding='utf8') as file:
    data = file.read()

# q1
# 1
def q1_1():
	return len(''.join(sorted(data)).split('()')[0])-len(''.join(sorted(data)).split('()')[1])

def q1_2():
    return data.count('(') - data.count(')')

def q1_XXX(data, f=0):
    f += 1 if data[0] == '(' else -1
    f += q1_XXX(data[1:])
    return f

# q2
# 1
def q2_1():
	f=0
	i=-1
	while(f>-1):
		i += 1
		f += 1 if data[i] == '(' else -1
	return i + 1

def q2_2():
	f=0
	i=0
	while(f>-1):
		i += 1
		f += 1 if data[i] == '(' else -1
	return i + 1

print(q1_XXX(data))










SOLUTION_1 = None

print(f"SOLUTION_1: {SOLUTION_1}")
