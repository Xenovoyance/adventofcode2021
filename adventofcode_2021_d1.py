import time

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

if __name__ == "__main__":
    start_time = time.time()
    print("Part 1: " + part_one() + " executed in " + str(time.time() - start_time) + " seconds")