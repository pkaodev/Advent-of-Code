import os
from math import inf as infinity
current_dir = os.path.dirname(os.path.realpath(__file__))
# input_path = os.path.join(os.path.dirname(__file__), 'input_example')
input_path = os.path.join(os.path.dirname(__file__), 'input')
# input_path = os.path.join(os.path.dirname(__file__), 'input_mega')

with open(input_path, 'r', encoding='utf8') as file:
    _data = file.read().split('\n\n')
    data = []
    for game in _data:
        game = game.replace('\n', ' ')
        xA = int(game.split('X+')[1].split(', Y+')[0])
        yA = int(game.split('Y+')[1].split(' Button')[0])
        xB = int(game.split('Button B: X+')[1].split(', Y+')[0])
        yB = int(game.split('Y+')[2].split(' Prize')[0])
        xFinal = int(game.split('Prize: X=')[1].split(', Y=')[0])
        yFinal = int(game.split('Y=')[1].split(' ->')[0])
        data.append((xA, yA, xB, yB, xFinal, yFinal))

def get_min_cost_1(xA, yA, xB, yB, xFinal, yFinal):
    A_COST = 3
    B_COST = 1
    
    cost = infinity
    maxA = xFinal // xA
    
    for numA in range(maxA + 1):
        _xFinal = xFinal - (numA * xA)
        _yFinal = yFinal - (numA * yA)
        
        numB = _xFinal / xB
        if numB % 1 != 0:
            continue
        if numB * yB != _yFinal:
            continue
        
        _cost = (A_COST * numA) + (B_COST * numB)
        cost = min(cost, _cost)
            
    return cost if cost is not infinity else 0
    
def solution_1(data):
    cost = 0
    
    for game in data:
        print(game)
        (xA, yA, xB, yB, xFinal, yFinal) = game
        cost += get_min_cost_1(xA, yA, xB, yB, xFinal, yFinal)
        
    print(int(cost))

# solution_1(data)

def get_min_cost_2(xA, yA, xB, yB, xFinal, yFinal):
    """
    Xf = An * Ax + Bn * Bx
    Yf = An * Ay + Bn * By
    
    An = (Xf * By - Yf * Bx) / (Ax * By - Bx * Ay)
    Bn = (-Xf * Ay + Yf * Ax) / (Ax * By - Bx * Ay)
    """
    
    A_COST = 3
    B_COST = 1
    
    num_A = (xFinal * yB - yFinal * xB) / (xA * yB - xB * yA)
    num_B = (yFinal * xA - xFinal * yA) / (xA * yB - xB * yA)
    print('num_A:', num_A, 'num_B', num_B)
    
    # they both need to be positive integers
    if num_A % 1 != 0 or num_B % 1 !=0:
        return 0
    
    return num_A * A_COST + num_B * B_COST

def solution_2(data):
    cost = 0
    
    for game in data:
        print(game)
        (xA, yA, xB, yB, xFinal, yFinal) = game
        # xFinal += 10000000000000
        # yFinal += 10000000000000
        cost += get_min_cost_2(xA, yA, xB, yB, xFinal, yFinal)
        
    print(cost)
    
solution_2(data)