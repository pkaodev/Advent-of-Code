import os
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input_example')
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    data = list(map(int, data[0].split(' ')))
    
def solution_1(data):
    num_gens = 25
    gen = 0
    
    while gen < num_gens:
        gen += 1
        print(gen)
        
        new_data = []
        
        for stone in data:
            if stone == 0:
                new_data.append(1)
            elif len(str(stone)) % 2 == 0:
                _stone = str(stone)
                left = _stone[:len(_stone)//2]
                right = _stone[len(_stone)//2:]
                new_data.append(int(left))
                new_data.append(int(right))
            else:
                new_data.append(stone*2024)
                
            data = new_data
        
    # print(new_data)
    print(len(new_data))

# solution_1(data)

def solution_2(data):
    
    _data = {}
    for _ in data:
        if _ in _data:
            _data[_] +=1
        else:
            _data[_] = 1
    data = _data
    
    num_gens = 75
    gen = 0
    
    while gen < num_gens:
        # print(data)
        gen += 1
        
        new_data = {}
        
        for stone_value in data:
            if stone_value == 0:
                if 1 not in new_data:
                    new_data[1] = data[0]
                else:
                    new_data[1] += data[0]
                    
            elif len(str(stone_value)) % 2 == 0:
                _stone = str(stone_value)
                left = _stone[:len(_stone)//2]
                right = _stone[len(_stone)//2:]
                
                if int(left) not in new_data:
                    new_data[int(left)] = data[stone_value]
                else:
                    new_data[int(left)] += data[stone_value]
                
                if int(right) not in new_data:
                    new_data[int(right)] = data[stone_value]
                else:
                    new_data[int(right)] += data[stone_value]
                    
            else:
                if stone_value*2024 not in new_data:
                    new_data[stone_value*2024] = data[stone_value]
                else:
                    new_data[stone_value*2024] += data[stone_value]
                
        data = new_data
        
    solution = 0
    for _ in data:
        solution += data[_]
    print(solution)

solution_2(data)
