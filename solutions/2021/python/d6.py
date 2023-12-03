current_day = 0
#list containing fish as integers (days until new spawn)
list_of_fish = []

input_string = ''
#fill list with input
with open("d6input", "r") as input:
   input_string = input.readline()

input_string = input_string.replace(',', '')
for i in input_string:
    list_of_fish.append(int(i))




fish_spawn_list = []
while current_day < 0:
   current_day += 1

   #tester
   number_of_fish = len(list_of_fish)
   print('Day {}: {} fish.'.format(current_day - 1, number_of_fish))
   print(list_of_fish)
   print(fish_spawn_list)
   fish_spawn_list = []

   for i in range(len(list_of_fish)):
       #if age is 0
       if list_of_fish[i] == 0:
           #spawn new fish
           fish_spawn_list.append(8)
           #change age to
           list_of_fish[i] = 6
       else:
           list_of_fish[i] -= 1

   for i in fish_spawn_list:
        list_of_fish.append(i)


number_of_fish = len(list_of_fish)
#print('\n\nNumber of fish after 80 days is {}\n\nEnd.'.format(number_of_fish))


####part 2
current_day = 0
dict_of_fish = {8:0, 7:0, 6:0, 5:0, 4:0, 3:0, 2:0, 1:0, 0:0}
input_string = ''

with open("d6input", "r") as input:
    input_string = input.readline()
input_string = input_string.replace(',', '')
for i in input_string:
    for j in range(9):
        if int(i) == j:
            dict_of_fish[j] += 1
        else:
            pass


while current_day < 256:
    total = sum(dict_of_fish.values())
    print('Day {}: {} fish.'.format(current_day, number_of_fish))
    current_day += 1
    number_of_spawn = 0

    for i in range(8):
        if i == 0:
            number_of_spawn = dict_of_fish[0]
            print('number of spawn is {}'.format(number_of_spawn))
            dict_of_fish[0] = dict_of_fish[1]
            print(dict_of_fish[0])
        else:
            dict_of_fish[i] = dict_of_fish[i+1]

    dict_of_fish[8] = number_of_spawn
    dict_of_fish[6] += number_of_spawn
    print('number of 8 fish is {}'.format(dict_of_fish[8]))



total = sum(dict_of_fish.values())
print('Final total after 256 days is {}'.format(total))
#NT INT INT