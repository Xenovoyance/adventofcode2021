import time
from collections import defaultdict

def input_to_string():
    input = "adventofcode_2021_d3_input.txt"
    input_string = []
    with open(input, "r") as f:
        for line in f.readlines():
            input_string.append(line.strip())
    return input_string, len(line.strip())

def part_one():
    data = input_to_string()
    binary_range = data[1]
    input_data = data[0]
    counter_one = {}
    counter_zero = {}
    gamma = epsilon = ""

    for a in input_data:
        for counter, b in enumerate(a):
            if b == "1":
                if counter not in counter_one:
                    counter_one[counter] = 0
                counter_one[counter] += 1 
            elif b == "0":
                if counter not in counter_zero:
                    counter_zero[counter] = 0
                counter_zero[counter] += 1 
    
    for diagnostics in range(binary_range):
        if (counter_one[diagnostics] - counter_zero[diagnostics]) > 0:
            gamma = gamma + "1"
            epsilon = epsilon + "0"
        else:
            gamma = gamma + "0"
            epsilon = epsilon + "1"
    gamma = int(gamma,2)
    epsilon = int(epsilon,2)

    return str(gamma * epsilon)
      

if __name__ == "__main__":
    start_time = time.time()
    print("Part 1: " + part_one() + " executed in " 
        + (str((time.time() - start_time)* 1000)) + " ms")