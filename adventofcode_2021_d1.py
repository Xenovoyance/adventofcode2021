import time

input = "adventofcode_2021_d1_input.txt"

def main():
    with open(input, "r") as f:
        lines = f.readlines()
        last_line = 0
        greater = 0
        for line in lines:
            if last_line < int(line): 
                if last_line != 0: greater += 1
            last_line = int(line)
        return(greater)

if __name__ == "__main__":
    start_time = time.time()
    print("Part 1:", main(), "(", time.time() - start_time, "seconds)")