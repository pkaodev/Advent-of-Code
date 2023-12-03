class Octopus:
    def __init__(self, y, x, energy_level):
        self.y = y
        self.x = x
        self.energy_level = energy_level
        self.has_flashed = 0

    def increase_energy_level(self):
        self.energy_level += 1

    def reset_flash(self):
        if self.has_flashed == 1:
            self.energy_level = 0
            self.has_flashed = 0

    def check_and_flash(self):
        if (self.energy_level > 9) and (self.has_flashed == 0):
            for y in range(-1,2):
                for x in range(-1,2):
                    if (x == 0) and (y == 0):
                        pass
                    elif (self.y+y < 0) or (self.x+x < 0):
                        pass
                    else:
                        try:
                            object_map[self.y+y][self.x+x].energy_level += 1
                        except IndexError:
                            pass
            self.has_flashed = 1




total_number_of_flashes = 0
current_step = 0

def print_list_by_row(lst):
    for row in lst:
        print(row)

def update_and_print_map():
    for row in range(len(current_map)):
        for octopus in range(len(current_map[0])):
            current_map[row][octopus] = object_map[row][octopus].energy_level
    print_list_by_row(current_map)

def create_octopus_objects():
    object_map = []
    for y in range(len(original_map)):
        object_map.append([Octopus(y, x, original_map[y][x]) for x in range(len(original_map[0]))])
    return(object_map)






def increase_all_energy_levels_by_one():
    for row in range(len(current_map)):
        for octopus in range(len(current_map[0])):
            object_map[row][octopus].increase_energy_level()


def reset_flash_all():
    for row in range(len(current_map)):
        for octopus in range(len(current_map[0])):
            object_map[row][octopus].reset_flash()

def check_flash_all():
    for row in range(len(current_map)):
        for octopus in range(len(current_map[0])):
            object_map[row][octopus].check_and_flash()
#if no flashes, stop look, go next step
#if flashes, check again

def count_flashes():
    flashes_this_step = 0
    for row in range(len(current_map)):
        for octopus in range(len(current_map[0])):
            if object_map[row][octopus].has_flashed:
                flashes_this_step += 1
    return flashes_this_step
###total_number_of_flashes += count_flashes()




##############################################################
original_map = []

with open('d11input', 'r') as input_file:
    for line in input_file:
        string = line.rstrip('\n')
        original_map.append([int(word) for word in string])

current_map = original_map

object_map = create_octopus_objects()

print('INITIAL')
update_and_print_map()

KEEP_GOING = 1
while KEEP_GOING == 1:
    current_step += 1
    increase_all_energy_levels_by_one()

    while True:
        initial = count_flashes()
        check_flash_all()
        second = count_flashes()
        if initial == second:
            break

    print('Results after {} step(s):'.format(current_step))
    print('Flashes this step: {}'.format(count_flashes()))

    total_number_of_flashes += count_flashes()
    if count_flashes() == 100:
        KEEP_GOING = 0

    reset_flash_all()
    update_and_print_map()
    #end while loop












print(total_number_of_flashes)

print(current_step)