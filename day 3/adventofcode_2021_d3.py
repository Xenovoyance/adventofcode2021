import time
from collections import defaultdict

def input_to_string():
    input = "adventofcode_2021_d3_input.txt"
    input_string = []
    with open(input, "r") as f:
        for line in f.readlines():
            input_string.append(line.strip())
    return input_string, len(line.strip())

def binary_counter(input_data, counter_one, counter_zero):
    for a in input_data:
        for counter, b in enumerate(a):
            if b == "1":
                if counter not in counter_one: counter_one[counter] = 0
                counter_one[counter] += 1 
            elif b == "0":
                if counter not in counter_zero: counter_zero[counter] = 0
                counter_zero[counter] += 1 
    return counter_one, counter_zero

def reduce_list(input_list, start_with):
    return [i for i in input_list if i.startswith(start_with)]

def part_one():
    input_data, binary_range = input_to_string()
    counter_one = {}
    counter_zero = {}
    gamma = epsilon = ""

    counter_one, counter_zero = binary_counter(input_data, counter_one, counter_zero)

    for diagnostics in range(binary_range):
        if (counter_one[diagnostics] - counter_zero[diagnostics]) > 0:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        elif (counter_one[diagnostics] - counter_zero[diagnostics]) < 0:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
    
    return str(int(gamma,2) * int(epsilon,2))
    
def part_two():
    input_data, binary_range = input_to_string()
    oxygen_data = co2_data = input_data
    counter_one = counter_zero = {}
    gamma = epsilon = oxygen = co2 = ""

    counter_one, counter_zero = binary_counter(input_data, counter_one, counter_zero)
 
    for diagnostics in range(binary_range):
        if (counter_one[diagnostics] - counter_zero[diagnostics]) > 0:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        elif (counter_one[diagnostics] - counter_zero[diagnostics]) < 0:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"

    for diagnostics in range(binary_range):
        counter_one = {}
        counter_zero = {}
        counter_one, counter_zero = binary_counter(oxygen_data, counter_one, counter_zero)
        if (counter_one[diagnostics] - counter_zero[diagnostics]) > 0:
            oxygen = oxygen + "1"
        elif (counter_one[diagnostics] - counter_zero[diagnostics]) < 0:
            oxygen = oxygen + "0"
        else:
            oxygen = oxygen + "1"
        oxygen_data = reduce_list(oxygen_data, str(oxygen))
        if len(oxygen_data) == 1:
            oxygen = str(oxygen_data[0])
            break

    for diagnostics in range(binary_range):
        counter_one = {}
        counter_zero = {}
        counter_one, counter_zero = binary_counter(co2_data, counter_one, counter_zero)
        if (counter_one[diagnostics] - counter_zero[diagnostics]) > 0:
            co2 = co2 + "0"
        elif (counter_one[diagnostics] - counter_zero[diagnostics]) < 0:
            co2 = co2 + "1"
        else:
            co2 = co2 + "0"
        co2_data = reduce_list(co2_data, str(co2))
        if len(co2_data) == 1:
            co2 = str(co2_data[0])
            break
    
    return str(int(oxygen,2) * int(co2,2))

if __name__ == "__main__":
    start_time = time.time()
    print("Day 3, part 1: " + part_one() + " executed in " 
        + (str((time.time() - start_time)* 1000)) + " ms")
    start_time = time.time()
    print("Day 3, part 2: " + part_two() + " executed in " 
        + (str((time.time() - start_time)* 1000)) + " ms")