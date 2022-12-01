parsed_list = []
gamma_rate_decimal = 0
gamma_rate_binary = ''
epsilon_rate_decimal = 0
epsilon_rate_binary = ''

with open("d3input", "r") as input:
    for line in input:
        parsed_list.append(line.rstrip('\n'))

for i in range(len(parsed_list[0])):
    counter_0 = 0
    counter_1 = 0
    for j in range(len(parsed_list)):
        if parsed_list[j][i] == '0':
            counter_0 += 1
        elif parsed_list[j][i] == '1':
            counter_1 += 1
    if counter_0 > counter_1:
        gamma_rate_binary += '0'
    elif counter_1 > counter_0:
        gamma_rate_binary += '1'


for k in range(len(parsed_list[0])):
    if gamma_rate_binary[k] == '0':
        epsilon_rate_binary += '1'
    elif gamma_rate_binary[k] == '1':
        epsilon_rate_binary += '0'

for l in range(len(parsed_list[0])):
    if gamma_rate_binary[l] == '1':
        gamma_rate_decimal += 2 ** (len(parsed_list[0]) - l -1)
    else:
        epsilon_rate_decimal += 2 ** (len(parsed_list[0]) - l -1)


print('parsed list')
print(parsed_list)

power_consumption = gamma_rate_decimal * epsilon_rate_decimal
print('power consumption: {}'.format(power_consumption))

###p2

###
oxy_gen_rating = parsed_list
print(oxy_gen_rating)


while len(oxy_gen_rating) > 1:
    for i in range(len(oxy_gen_rating[0])):
        counter_0 = 0
        counter_1 = 0
        #######
        for j in range(len(oxy_gen_rating)):
            if oxy_gen_rating[j][i] == '0':
                counter_0 += 1
            else:
                counter_1 += 1

        if counter_1 >= counter_0:
            for line in oxy_gen_rating:
                if line[i] == '0':
                    if len(oxy_gen_rating) > 1:
                        print('removing {}'.format(line))
                        oxy_gen_rating.remove(line)
                else:
                    pass

        elif counter_0 > counter_1:
            for line in oxy_gen_rating:
                if line[i] == '1':
                    if len(oxy_gen_rating) > 1:
                        print('removing {}'.format(line))
                        oxy_gen_rating.remove(line)
                else:
                    pass


parsed_list = []
with open("d3input", "r") as input:
    for line in input:
        parsed_list.append(line.rstrip('\n'))
co2_scrub_rating = parsed_list

while len(co2_scrub_rating) > 1:
    for i in range(len(co2_scrub_rating[0])):
        counter_0 = 0
        counter_1 = 0
        for j in range(len(co2_scrub_rating)):
            if co2_scrub_rating[j][i] == '0':
                counter_0 += 1
            else:
                counter_1 += 1

        if counter_1 >= counter_0:
            for line in co2_scrub_rating:
                if line[i] == '1':
                    if len(co2_scrub_rating) > 1:
                        print('removing {}'.format(line))
                        co2_scrub_rating.remove(line)
                else:
                    pass

        elif counter_0 > counter_1:
            for line in co2_scrub_rating:
                if line[i] == '0':
                    if len(co2_scrub_rating) > 1:
                        print('removing {}'.format(line))
                        co2_scrub_rating.remove(line)
                else:
                    pass

print('oxy')
print(oxy_gen_rating)
print('co2')
print(co2_scrub_rating)

oxy_dec = 0
co2_dec = 0


for l in range(len(oxy_gen_rating[0])):
    if oxy_gen_rating[0][l] == '1':
        oxy_dec += 2 ** (len(parsed_list[0]) - l -1)
    else:
        pass

for l in range(len(co2_scrub_rating[0])):
    if co2_scrub_rating[0][l] == '1':
        co2_dec += 2 ** (len(parsed_list[0]) - l -1)
    else:
        pass

print(oxy_dec)
print(co2_dec)

solution = oxy_dec * co2_dec
print(solution)