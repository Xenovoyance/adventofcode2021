import time

class BingoBoard:
    def __inti__(self, id, numbers):
        self.id = id
        for number in numbers:
            self.numbers.append(number)

def part_one():
    input = "adventofcode_2021_d4_input.txt"
    input_string = []
    with open(input, "r") as f:
        for id, line in enumerate(f.readlines()):
            input_string.append(line.strip().split())
            print(input_string)
    return input_string
        

if __name__ == "__main__":
    #start_time = time.time()
    #print("Part 1: " + part_one() + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")
    part_one()