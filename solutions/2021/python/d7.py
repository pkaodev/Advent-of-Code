crab_list = []
final_position = 0
fuel_cost_list = []

with open("d7input", "r") as input_file:
    input_string = input_file.readline()
    crab_list = [int(i) for i in input_string.split(',')]

for i in range(min(crab_list), max(crab_list)+1):
    fuel_cost = 0
    for crab in crab_list:
       fuel_cost += ((abs(crab - i) * (abs(crab - i) + 1)) / 2)
    fuel_cost_list.append(fuel_cost)




print(fuel_cost_list)
print(min(fuel_cost_list))
print(max(fuel_cost_list))
print(fuel_cost_list.index(min(fuel_cost_list)))
#find index of min(fuel_cost_list)