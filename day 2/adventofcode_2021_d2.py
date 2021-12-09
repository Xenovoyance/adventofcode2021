import time

def input_to_string():
    input = "adventofcode_2021_d2_input.txt"
    input_string = []
    with open(input, "r") as f:
        for line in f.readlines():
            input_string.append(line.strip().split())
    return input_string

def part_one():
    input_string = input_to_string()
    depth = horizontal = 0
    
    for sub_move_key, sub_move_amount in input_string:
        if sub_move_key == "forward":
            horizontal += int(sub_move_amount)
        elif sub_move_key == "down":
            depth += int(sub_move_amount)
        elif sub_move_key == "up":
            depth -= int(sub_move_amount)
    
    return str(depth * horizontal)

def part_two():
    input_string = input_to_string()
    depth = horizontal = aim = 0
    
    for sub_move_key, sub_move_amount in input_string:
        if sub_move_key == "forward":
            horizontal += int(sub_move_amount)
            depth += (aim * int(sub_move_amount))
        elif sub_move_key == "down":
            aim += int(sub_move_amount)
        elif sub_move_key == "up":
            aim -= int(sub_move_amount)
    
    return str(depth * horizontal)
        

if __name__ == "__main__":
    start_time = time.time()
    print("Part 1: " + part_one() + " executed in " 
        + (str((time.time() - start_time)* 1000)) + " ms")
    start_time = time.time()
    print("Part 2: " + part_two() + " executed in " 
        + (str((time.time() - start_time)*1000)) + " ms")