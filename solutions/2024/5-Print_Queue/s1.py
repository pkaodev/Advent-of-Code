import os
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input_example')
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    
def solution_1(data):
    _rules = data[:data.index('')]
    _updates = data[data.index('')+1:]
    
    rules = {}
    for rule in _rules:
        a, b = rule.split('|')
        if a not in rules:
            rules[a] = [b]
        else:
            rules[a].append(b)
    
    updates = [_.split(',') for _ in _updates]
         
    solution = 0
       
    for update in updates:
        is_valid = True
        for i in range(len(update)-1, 0, -1):
            if not is_valid:
                break
            for j in range(i-1, -1, -1):
                
                if update[j] not in rules:
                    is_valid = False
                    break
                
                if update[i] not in rules[update[j]]:
                    is_valid = False
                    break
                    
        if is_valid:
            solution += int(update[len(update)//2]) 
            
    print(solution)
        
# solution_1(data)

def solution_2(data):
    _rules = data[:data.index('')]
    _updates = data[data.index('')+1:]
    
    rules = {}
    for rule in _rules:
        a, b = rule.split('|')
        if int(a) not in rules:
            rules[int(a)] = [int(b)]
        else:
            rules[int(a)].append(int(b))
    
    updates = [
        [int(_2) for _2 in _1.split(',')]
        for _1 in _updates
    ]
         
    wrong_things = []
       
    for update in updates:
        break_that_shit = False
        for i in range(len(update)-1, 0, -1):
            if break_that_shit:
                break # that shit
            for j in range(i-1, -1, -1):
                if update[j] not in rules:
                    break_that_shit = True
                    wrong_things.append(update)
                    break
                
                if update[i] not in rules[update[j]]:
                    break_that_shit = True
                    wrong_things.append(update)
                    break
    
    print(wrong_things)
            
    solution = 0
    # print(rules)
    
    for thing in wrong_things:
        new_thing = []
        # print(thing)
        
        i = -1
        
        while len(thing) > 0:
            i = (i + 1) % len(thing)
            
            if thing[i] not in rules:
                new_thing.append(thing.pop(i))
                continue
            
            ok = True
            for _ in thing:
                if _ in rules[thing[i]]:
                    ok = False
                    break
            
            if ok:
                new_thing.append(thing.pop(i))
                continue
        
        print(new_thing)   
        # print(int(new_thing[len(new_thing)//2]))
        solution += int(new_thing[len(new_thing)//2])
        
        
    print(solution)


solution_2(data)

