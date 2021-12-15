import time
import numpy as np

def part_one():
    input = "adventofcode_2021_d5_input.txt"
    
    with open(input, "r") as f:
        x = []
        y = []
        x_max = y_max = 0
        for line in f.readlines():
            x1 = int(line.strip().replace(" -> ",",").split(',')[0])
            x2 = int(line.strip().replace(" -> ",",").split(',')[2])
            y1 = int(line.strip().replace(" -> ",",").split(',')[1])
            y2 = int(line.strip().replace(" -> ",",").split(',')[3])
            
            x.append([x1, x2])
            y.append([y1 ,y2])

            x_max = max(int(x_max), int(x1), int(x2))
            y_max = max(int(y_max), int(y1), int(y2))

    matrix = np.zeros((x_max+1, y_max+1), dtype=int)

    for i in range(len(x)):
        x1, x2 = x[i]
        y1, y2 = y[i]
        if x1 == x2:
            matrix[y1][x1] += 1
            matrix[y2][x2] += 1
            y_difference = y1 - y2
            
            if y_difference>1:
                for i in range(1,abs(y_difference)):
                    matrix[y1-i][x1] += 1
            else:
                for i in range(1,abs(y_difference)):
                    matrix[y1+i][x1] += 1
        
        if y1 == y2:
            matrix[y1][x1] += 1
            matrix[y2][x2] += 1
            x_difference = x1 - x2

            if x_difference>0:
                for i in range(1,abs(x_difference)):
                    matrix[y2][x2+i] += 1
            else:
                for i in range(1,abs(x_difference)):
                    matrix[y2][x2-i] += 1

    return str(len(np.where(matrix >= 2)[0]))

if __name__ == "__main__":
    start_time = time.time()
    print("Day 5, part 1: " + part_one() + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")
    #start_time = time.time()
    #print("Part 2: " + part_two() + " executed in " + (str((time.time() - start_time)*1000)) + " ms")

    #part_one()
