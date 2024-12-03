import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    data = data[0] if len(data) is 1 else data
    
print(data)

# q1
# num unique coords visited




def q1_1(data):
	x = 0
	y = 0
	visited = {'0,0',}
 
	def up():
		nonlocal y
		y += 1
  
	def down():
		nonlocal y
		y -= 1
  
	def right():
		nonlocal x
		x += 1
  
	def left():
		nonlocal x
		x -= 1
  
	move = {
		'^': up,
		'v': down,
		'>': right,
		'<': left
	}
 
	for d in data:
		move[d]()
		visited.add(f"{x},{y}")
  
	return len(visited)

# q2
def q2_1(data):

	visited = {'0,0',}
  
	move = {
			'^': ('y',1),
			'v': ('y',-1),
			'>': ('x',1),
			'<': ('x',-1),
	}
 
	coords = {
		'santa':{
			'x': 0,
			'y': 0
		},
		'robo':{
			'x': 0,
			'y': 0
		},
	}
 
 
	curr = 'santa'

	for d in data:
		curr = 'santa' if curr == 'robo' else 'robo'

		direction, value = move[d]
		
		coords[curr][direction] += value
  
		visited.add(f"{coords[curr]['x']},{coords[curr]['y']}")
		
  
	return len(visited)

print(q2_1(data))
