import time
import more_itertools

def input_to_string():
    input = "adventofcode_2021_d1_input.txt"
    input_string = []
    with open(input, "r") as f:
        for line in f.readlines():
            input_string.append(int(line))
    return input_string

def part_one():
    input_string = input_to_string()
    last_line = greater = 0

    for line in input_string:
        if last_line < int(line) and last_line != 0: greater += 1
        last_line = int(line)
    return(str(greater))

def part_two():
    last_window = greater = 0
    input_string = input_to_string()
        
    window_list = list(more_itertools.windowed(input_string,n=3, step=1))
    for window in window_list:
        window_sum = sum(window)
        if window_sum > last_window and last_window != 0: greater += 1
        last_window = window_sum
    return str(greater)
        

if __name__ == "__main__":
    start_time = time.time()
    print("Part 1: " + part_one() + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")
    start_time = time.time()
    print("Part 2: " + part_two() + " executed in " + (str((time.time() - start_time)*1000)) + " ms")