import os
current_dir = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(os.path.dirname(__file__), 'input')

with open(input_path, 'r', encoding='utf8') as file:
    data = file.read().split('\n')
    data = data[0] if len(data) == 1 else data
    
def q1_s1(data):
    """
    wire_values = {
        'a': {
            'wire_dependencies': ['b', 'c'], # 0/1/2
            'operator': 'AND', # NOT/OR/AND/RSHIFT/LSHIFT
            'operator_value': None, # None or int
            'value': None # None or int (value)
        }
    }
    """
    def is_int(str_val):
        try:
            int_val = int(str_val)
        except:
            int_val = None
        return int_val
       
    def parse_input(data):
        wire_values = {}
        for line in data:
            resulting_wire = line.split('-> ')[1]
            value = is_int(line.split( '-> ')[0])
            
            if line.split(' ')[0] == 'NOT':
                operator = 'NOT'
            elif len(line.split(' -> ')) == 2:
                operator = None
            else:
                operator = line.split(' ')[1]
                
            wire_dependencies = []
            if operator == 'NOT':
                if is_int(line.split(' ')[1]) is None:
                    wire_dependencies.append(line.split(' ')[1])
            elif operator is None:
                if is_int(line.split(' ')[0]) is None:
                    wire_dependencies.append(line.split(' ')[0])
            else:
                if is_int(line.split(' ')[0]) is None:
                    wire_dependencies.append(line.split(' ')[0])
                if is_int(line.split(' ')[2]) is None:
                    wire_dependencies.append(line.split(' ')[2])
            
            wire_values[line.split('-> ')[1]] = {
                'value': 
            }
        pass

    return 22 >> 1

print(q1_s1(data))