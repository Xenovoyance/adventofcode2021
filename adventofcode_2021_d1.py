import itertools
import time
import more_itertools

input = "adventofcode_2021_d1_input.txt"

def part_one():
    with open(input, "r") as f:
        lines = f.readlines()
        last_line = greater = 0
        for line in lines:
            if last_line < int(line): 
                if last_line != 0: greater += 1
            last_line = int(line)
        return(str(greater))

def part_two():
    last_line = greater = 0
    input_string = []
    
    with open(input, "r") as f:
        for line in f.readlines():
            input_string.append(int(line))
        
        tuple_list = list(more_itertools.windowed(input_string,n=3, step=1))

        for tuple in tuple_list:
            tuple_sum = sum(tuple)
            if tuple_sum > last_line and last_line != 0: greater += 1
            last_line = tuple_sum

        return str(greater)
        

if __name__ == "__main__":
    start_time = time.time()
    print("Part 1: " + part_one() + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")
    start_time = time.time()
    print("Part 2: " + part_two() + " executed in " + (str((time.time() - start_time)*1000)) + " ms")