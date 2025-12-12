import os
import sys
import math

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
    def distance(a, b):
        return math.sqrt(
            ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)
        )

    # (x,y,z)
    junction_boxes = []  # (x,y,z)
    all_pair_distances = []  # unsorted (index_a, index_b, distance) index of boxes
    for i, row in enumerate(data):
        parts = row.split(",")
        junction_box = (int(parts[0]), int(parts[1]), int(parts[2]))
        for j in range(len(junction_boxes) - 1):
            calculated_distance = distance(junction_box, junction_boxes[j])
            all_pair_distances.append((i, j, calculated_distance))
        junction_boxes.append(junction_box)

    # sort by distance
    all_pair_distances.sort(key=lambda x: x[2])

    circuits = []  # [{index_a, index_b, ...}, ...]
    first_circuit_pair = all_pair_distances.pop(0)
    circuits.append({first_circuit_pair[0], first_circuit_pair[1]})

    NUM_CONNECTIONS = 1
    MAX_CONNECTIONS = 1000

    for pair in all_pair_distances:
        if NUM_CONNECTIONS == MAX_CONNECTIONS:
            break

        first_box_index, second_box_index = (
            pair[0],
            pair[1],
        )

        found = False
        for _x, circuit in enumerate(circuits):
            first_box_in_circuit = first_box_index in circuit
            second_box_in_circuit = second_box_index in circuit
            if first_box_in_circuit and second_box_in_circuit:
                found = True
                break

            if first_box_in_circuit:
                # if B is in some other circuit combine circuits
                second_box_circuit_found = False
                for i in range(len(circuits)):
                    if second_box_index in circuits[i]:
                        circuits[_x] = circuit.union(circuits[i])
                        circuits.pop(i)
                        found = True
                        second_box_circuit_found = True
                        break

                if not second_box_circuit_found:
                    circuit.add(second_box_index)

                found = True
                break

            if second_box_in_circuit:
                # if A is in some other circuit combine circuits
                first_box_circuit_found = False
                for i in range(len(circuits)):
                    if first_box_index in circuits[i]:
                        circuits[_x] = circuit.union(circuits[i])
                        circuits.pop(i)
                        found = True
                        first_box_circuit_found = True
                        break

                if not first_box_circuit_found:
                    circuit.add(first_box_index)

                found = True
                break

        if not found:
            circuits.append({first_box_index, second_box_index})

        NUM_CONNECTIONS += 1

    circuit_sizes = list(map(len, circuits))
    three_largest = sorted(circuit_sizes)[-3:]
    tl = three_largest
    result = tl[0] * tl[1] * tl[2]
    print(result)


def solution_2(data):
    def distance(a, b):
        return math.sqrt(
            ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)
        )

    # (x,y,z)
    junction_boxes = []  # (x,y,z)
    all_pair_distances = []  # unsorted (index_a, index_b, distance) index of boxes
    for i, row in enumerate(data):
        parts = row.split(",")
        junction_box = (int(parts[0]), int(parts[1]), int(parts[2]))
        for j in range(len(junction_boxes) - 1):
            calculated_distance = distance(junction_box, junction_boxes[j])
            all_pair_distances.append((i, j, calculated_distance))
        junction_boxes.append(junction_box)

    # sort by distance
    all_pair_distances.sort(key=lambda x: x[2])

    circuits = []  # [{index_a, index_b, ...}, ...]
    first_circuit_pair = all_pair_distances.pop(0)
    circuits.append({first_circuit_pair[0], first_circuit_pair[1]})

    for i, current_pair_distance in enumerate(all_pair_distances):
        first_box_index, second_box_index = (
            current_pair_distance[0],
            current_pair_distance[1],
        )

        # are both the boxes in the current pair in any connected circuits?
        found = False
        # check each circuit
        for circuit_index, circuit in enumerate(circuits):
            first_box_in_circuit = first_box_index in circuit
            second_box_in_circuit = second_box_index in circuit

            # both boxes already in same circuit, connected indirectly before
            if first_box_in_circuit and second_box_in_circuit:
                found = True
                break

            # if one box is in the circuit, check if the other box is:
            # - not in any other circuit -> add box to circuit
            # - in another connected circuit -> combine circuit sets

            # only first box is in the circuit
            if first_box_in_circuit:
                # check if the second box is in another circuit
                second_box_circuit_found = False
                for i in range(len(circuits)):
                    if second_box_index in circuits[i]:
                        # yes -> combine circuit sets
                        circuits[circuit_index] = circuit.union(circuits[i])
                        circuits.pop(i)
                        found = True
                        second_box_circuit_found = True
                        break

                # no -> add box index to circuit
                if not second_box_circuit_found:
                    circuit.add(second_box_index)

                found = True
                break

            # only second box is in the circuit
            if second_box_in_circuit:
                # check if the first box is in another circuit
                first_box_circuit_found = False
                for i in range(len(circuits)):
                    # yes -> combine circuit sets
                    if first_box_index in circuits[i]:
                        circuits[circuit_index] = circuit.union(circuits[i])
                        circuits.pop(i)
                        found = True
                        first_box_circuit_found = True
                        break

                # no -> add box index to circuit
                if not first_box_circuit_found:
                    circuit.add(first_box_index)

                found = True
                break

        # neither box is in any circuit -> create new circuit
        if not found:
            circuits.append({first_box_index, second_box_index})

        # all boxes are in the same circuit -> calculate solution
        if len(circuits) == 1 and len(circuits[0]) == len(junction_boxes):
            solution = (
                junction_boxes[first_box_index][0] * junction_boxes[second_box_index][0]
            )
            print(solution)
            break


if __name__ == "__main__":
    solution_1(data)
    solution_2(data)
# P1 example solution: 1000
