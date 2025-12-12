import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.join(current_dir, "../../../templates/python")
sys.path.append(utils_path)
import utils

# input_file = "input_example"
input_file = "input"

input_path = os.path.join(current_dir, input_file)

with open(input_path, "r", encoding="utf8") as file:
    data = file.read().split("\n")

def solution_1(data):
    # print(data)

    ranges = []

    while True:
        val = data[0]
        data = data[1:]

        if not val:
            break

        low, high = val.split("-")
        ranges.append((int(low), int(high)))

    print(ranges)

    result = 0

    for fruit in data:
        print(fruit)
        for _range in ranges:
            if _range[0] <= int(fruit) <= _range[1]:
                result += 1
                break

    # 798
    print(result)



def solution_2(data):
    # print(data)

    ranges = []

    while True:
        val = data[0]
        data = data[1:]

        if not val:
            break

        low, high = val.split("-")
        ranges.append((int(low), int(high)))

    # print(ranges)
    
    
    def compact_ranges(ranges):
        print("START", ranges)
        if len(ranges) == 1:
            return ranges
        
        final_ranges = [ranges[0]]
        ranges = ranges[1:]
        print(final_ranges, ranges)
        
        while ranges:
            low_a, high_a = ranges[0]
            ranges = ranges[1:]
            
            overlapped = False
            for i, existing in enumerate(final_ranges):
                # print(i, existing)
                low_b, high_b = existing
                # if there is any overlap, then new range is min(minA, minB)->max(maxA, maxB)
                if low_b <= low_a <= high_b or low_b <= high_a <= high_b or low_a <= low_b <= high_a or low_a <= high_b <= high_a:
                    final_ranges[i] = (min(low_a, low_b), max(high_a, high_b))
                    overlapped = True
                    break
                
            if not overlapped:
                final_ranges.append((low_a, high_a))
                
            overlapped = False
                
        print("END", final_ranges)
        return final_ranges
                
    
    
    num_ranges_start = len(ranges)
    num_ranges_end = 0
    
    # print(">!>!>!>!>!>!>!>!>")
    # print()
    
    while num_ranges_start != num_ranges_end:
        # print(1, ranges)
        num_ranges_start = len(ranges)
        ranges = compact_ranges(ranges)
        num_ranges_end = len(ranges)
        # print(2, ranges)
        
    print(ranges)
    result = sum([
        pair[1] - pair[0] + 1
        for pair in ranges
    ])
        
    print(num_ranges_start, num_ranges_end)
    print(result)
        
                
        
        
        

if __name__ == "__main__":
    # solution_1(data)
    solution_2(data)
# P1 example solution: 3