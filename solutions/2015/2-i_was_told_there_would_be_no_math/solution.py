import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read()
    data_lines = data.split('\n')
    
print(data_lines)
# q1
# 2*l*w + 2*w*h + 2*h*l
# + smallest side area
def q1_1(data_lines):
    total = 0
    for present in data_lines:
        w, h, l = map(
            # lambda s: int(s),
            int,
            present.split('x')
        )
        total += 2 * (w*h + w*l + h*l) + min(w*h, w*l, h*l)
    return total

# q2
# smallest perimiter + volume
def q2_1(data_lines):
	total = 0
	for present in data_lines:
		w, h, l = map(
			int,
			present.split('x')
		)
		total += (2 * min(w+h, w+l, h+l)) + (w*h*l)
	return total

print(q2_1(data_lines))
