import os
import re
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input')
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    data = ''.join(data)
    
def solution_1(data):
	solution = 0
	_i1 = None
	_i2 = None
	for i in range(0, len(data)):
		if data[i] == 'm':
			_i1 = i
		if data[i] == ')':
			_i2 = i

		if _i1 is not None and _i2 is not None:
			print(data[_i1:_i2+1])
			_extracted_vals = extract_vals(data[_i1:_i2+1])
			if _extracted_vals is not None:
				solution += _extracted_vals[0] * _extracted_vals[1]
				_i1 = None
				_i2 = None

	print(solution)

def extract_vals(exp):
	my_regex = r'mul\((\d{1,3}),(\d{1,3})\)'
	match = re.match(my_regex, exp)
	if match:
		return (int(match.group(1)), int(match.group(2)))
	else:
		return None

def extract_do_dont(exp):
	do_regex = r'do\(\)'
	dont_regex = r"don't\(\)"

	do_match = re.match(do_regex, exp)
	dont_match = re.match(dont_regex, exp)

	if do_match:
		return "do"
	elif dont_match:
		return "dont"
	else:
		return None

def solution_2(data):
	solution = 0
	do_enabled = True
 
	# mul values
	_i1 = None
	_i2 = None
 
	# do/dont
	_i3 = None
	_i4 = None
 
	for i in range(0, len(data)):
		if data[i] == 'm':
			_i1 = i
		if data[i] == ')':
			_i2 = i

		if data[i] == 'd':
			_i3 = i
		if data[i] == ')':
			_i4 = i

		if _i3 is not None and _i4 is not None:
			_extracted_vals = extract_do_dont(data[_i3:_i4+1])
			if _extracted_vals is not None:
				if _extracted_vals == "do":
					do_enabled = True
				else:
					do_enabled = False
				_i3 = None
				_i4 = None

		if _i1 is not None and _i2 is not None:
			_extracted_vals = extract_vals(data[_i1:_i2+1])
			if _extracted_vals is not None:
				if do_enabled:
					solution += _extracted_vals[0] * _extracted_vals[1]
				_i1 = None
				_i2 = None


	print(solution)


# solution_1(data)
solution_2(data)