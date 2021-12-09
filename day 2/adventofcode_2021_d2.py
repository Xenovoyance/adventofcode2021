import time
import more_itertools

def input_to_string():
    input = "adventofcode_2021_d2_input.txt"
    input_string = []
    with open(input, "r") as f:
        for line in f.readlines():
            input_string.append(int(line))
    return input_string

def part_one():
    input_string = input_to_string()
    depth = horizontal = 0
    return(input_string)

def part_two():
    input_string = input_to_string()
        

if __name__ == "__main__":
    start_time = time.time()
    print("Part 1: " + part_one() + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")
    #start_time = time.time()
    #print("Part 2: " + part_two() + " executed in " + (str((time.time() - start_time)*1000)) + " ms")