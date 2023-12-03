def SortString(str):
    return ''.join(sorted(str))
def SortList(list):
    for i in range(len(list)):
        list[i] = SortString(list[i])
input_list = []
with open('d8input', 'r') as input_file:
    for line in input_file:
        print(line)
        temp_string = line.replace('\n', '')
        print(temp_string)
        temp_list = temp_string.split(' | ')
        print(temp_list)
        input_list.append(temp_list)



print(input_list)
print(len(input_list))

signal_list = []
output_list = []
total_list = []

for i in input_list:
    signal_list.append(i[0].split(' '))
    output_list.append(i[1].split(' '))
    total_list.append(i[0].split(' ') + i[1].split(' '))
SortList(signal_list)
SortList(output_list)
SortList(total_list)
print(len(input_list))
print(input_list)
print(len(signal_list))
print(signal_list)
print(len(output_list))
print(output_list)
print(len(total_list))
print(total_list)

answer = 0
for i in output_list:
    for j in range(4):
        if (len(i[j]) == 2) or (len(i[j]) == 4) or (len(i[j]) == 7) or (len(i[j]) == 3):
            answer += 1

print(answer)



output_test = 0
input_test1 = 'cf'
input_test2 = ''
input_test3 = ''
input_test4 = ''

if ('a' in input_test1) and ('b' in input_test1) and ('c' in input_test1) and ('e' in input_test1) and ('f' in input_test1) and ('g' in input_test1):
    output_test += 1000
if ('c' in input_test1) and ('f' in input_test1):
        output_test += 1

print(output_test)
all_letters = 'abcdefg'
real_0 = 'abcefg'
real_1 = 'cf'
real_2 = 'abcdeg'
real_3 = 'acdfg'
real_4 = 'bcdf'
real_5 = 'abdfg'
real_6 = 'abdefg'
real_7 = 'acf'
real_8 = 'abcdefg'
real_9 = 'abcdfg'
a = ''
b = ''
c = ''
d = ''
e = ''
f = ''
g = ''
zero = ''
one = ''
two = ''
three = ''
four = ''
five = ''
six = ''
seven = ''
eight = ''
nine = ''
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
for line in total_list:


    for word in line:
        if len(word) == 2:
            one = SortString(word)
            print('one is {}'.format(one))
        elif len(word) == 4:
            four = SortString(word)
            print('four is {}'.format(four))
        elif len(word) == 3:
            seven = SortString(word)
            print('seven is {}'.format(seven))
        elif len(word) == 7:
            eight = SortString(word)
            print('eight is {}'.format(eight))
        else:
            pass
    #a
    for letter in seven:
        if letter not in one:
            a = letter
            print('corrected a is {}'.format(a))
    #g
    temp_one = SortString(four + a)
    temp_one = sorted(temp_one)
    print('temp_one is {}'.format(temp_one))
    print(temp_one)
    for word in line:
        print(temp_one in sorted(word))
        print(len(word) == 6)
        if (temp_one in sorted(word)) and (len(word) == 6):
            print('1')
            for letter in word:
                if letter not in temp_one:
                    print('G')
                    g = letter

print()
print()
print(one,
      two,
three,
four,
five,
six,
seven,
eight,
nine)

print(a,
      b,
      c,
      d,
      e,
      f,
      g)

#a

#b

#c

#d

#e

#f

#g


#for i in input