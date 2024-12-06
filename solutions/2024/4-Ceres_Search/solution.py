import os
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input_example')
# input_path = os.path.join(os.path.dirname(__file__), 'input_example_2')
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    
def solution_1(data):
	min_x = 0
	max_x = len(data[0]) - 1
	min_y = 0
	max_y = len(data) - 1

	solution = 0

	dirs = [
		{"x":0,"y":1},
		{"x":1,"y":1},
		{"x":1,"y":0},
		{"x":1,"y":-1},
		{"x":0,"y":-1},
		{"x":-1,"y":-1},
		{"x":-1,"y":0},
		{"x":-1,"y":1}
	]

	for x in range (min_x, max_x + 1):
		for y in range (min_y, max_y + 1):
			
			for dir in dirs:
				if ((x + 3*dir["x"]) < min_x) or ((x + 3*dir["x"]) > max_x) or ((y + 3*dir["y"]) < min_y) or ((y + 3*dir["y"]) > max_y):
					continue
 
				if data[y][x] == "X":
						if data[y+dir["y"]][x+dir["x"]] == "M":
							if data[y+2*dir["y"]][x+2*dir["x"]] == "A":
								if data[y+3*dir["y"]][x+3*dir["x"]] == "S":
									solution += 1

	print(solution)

# solution_1(data)

def solution_2(data):
	min_x = 0
	max_x = len(data[0]) - 1
	min_y = 0
	max_y = len(data) - 1

	solution = 0

	for x in range (min_x, max_x + 1):
		for y in range (min_y, max_y + 1):
			
			if ((x + - 1) < min_x) or ((x + 1) > max_x) or ((y - 1) < min_y) or ((y +1) > max_y):
				continue

			if data[y][x] == "A":
				if ((data[y-1][x-1] == "M" and data[y+1][x+1] == "S") or (data[y-1][x-1] == "S" and data[y+1][x+1] == "M")) and ((data[y+1][x-1] == "M" and data[y-1][x+1] == "S") or (data[y+1][x-1] == "S" and data[y-1][x+1] == "M")):
					solution += 1
       
	print(solution)

solution_2(data)