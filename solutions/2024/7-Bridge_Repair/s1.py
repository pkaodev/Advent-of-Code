import os
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input_example')
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    
def solution_1(data):    
    solution = 0
    
    for line in data:
        result = int(line.split(':')[0])
        nums = [int(_) for _ in line.split(': ')[1].split(' ')]
        
        index = 0
        
        possible_results = [nums[0]]
        
        while index < len(nums) - 1:
            index += 1
            
            new_results_add = [
                _ + nums[index]
                for _ in possible_results
            ]
            new_results_mult = [
                _ * nums[index]
                for _ in possible_results
            ]
            
            possible_results = new_results_add + new_results_mult
            
        if result in possible_results:
            solution += result
            
    print(solution)
        
# solution_1(data)

def solution_2(data):    
    solution = 0
    
    for line in data:
        result = int(line.split(':')[0])
        nums = [int(_) for _ in line.split(': ')[1].split(' ')]
        
        index = 0
        
        possible_results = [nums[0]]
        
        while index < len(nums) - 1:
            index += 1
            
            new_results_add = [
                _ + nums[index]
                for _ in possible_results
            ]
            new_results_mult = [
                _ * nums[index]
                for _ in possible_results
            ]
            new_results_concat = [
                int(f'{_}{nums[index]}')
                for _ in possible_results
            ]
            
            possible_results = new_results_add + new_results_mult + new_results_concat
            
        if result in possible_results:
            solution += result
            
    print(solution)
        
solution_2(data)

