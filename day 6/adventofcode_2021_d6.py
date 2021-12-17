import time

def part_one():
    start_time = time.time()
    #input = "1,1,1,1,2,1,1,4,1,4,3,1,1,1,1,1,1,1,1,4,1,3,1,1,1,5,1,3,1,4,1,2,1,1,5,1,1,1,1,1,1,1,1,1,1,3,4,1,5,1,1,1,1,1,1,1,1,1,3,1,4,1,1,1,1,3,5,1,1,2,1,1,1,1,4,4,1,1,1,4,1,1,4,2,4,4,5,1,1,1,1,2,3,1,1,4,1,5,1,1,1,3,1,1,1,1,5,5,1,2,2,2,2,1,1,2,1,1,1,1,1,3,1,1,1,2,3,1,5,1,1,1,2,2,1,1,1,1,1,3,2,1,1,1,4,3,1,1,4,1,5,4,1,4,1,1,1,1,1,1,1,1,1,1,2,2,4,5,1,1,1,1,5,4,1,3,1,1,1,1,4,3,3,3,1,2,3,1,1,1,1,1,1,1,1,2,1,1,1,5,1,3,1,4,3,1,3,1,5,1,1,1,1,3,1,5,1,2,4,1,1,4,1,4,4,2,1,2,1,3,3,1,4,4,1,1,3,4,1,1,1,2,5,2,5,1,1,1,4,1,1,1,1,1,1,3,1,5,1,2,1,1,1,1,1,4,4,1,1,1,5,1,1,5,1,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,3,2,4,1,1,2,1,1,3,2".split(",")
    input = "3,4,3,1,2".split(",")

    for i in range(1,257):
        input_length = len(input)
        for j in range(0,input_length):
            if int(input[j])>0:
                input[j]=int(input[j])-1
            else:
                input[j] = 6
                input.append(8)
        print("Day 6, pt 1 ("+str(i)+" days): " + str(len(input)) + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")

def part_two():
    start_time = time.time()
    lanternfishes = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    input = "1,1,1,1,2,1,1,4,1,4,3,1,1,1,1,1,1,1,1,4,1,3,1,1,1,5,1,3,1,4,1,2,1,1,5,1,1,1,1,1,1,1,1,1,1,3,4,1,5,1,1,1,1,1,1,1,1,1,3,1,4,1,1,1,1,3,5,1,1,2,1,1,1,1,4,4,1,1,1,4,1,1,4,2,4,4,5,1,1,1,1,2,3,1,1,4,1,5,1,1,1,3,1,1,1,1,5,5,1,2,2,2,2,1,1,2,1,1,1,1,1,3,1,1,1,2,3,1,5,1,1,1,2,2,1,1,1,1,1,3,2,1,1,1,4,3,1,1,4,1,5,4,1,4,1,1,1,1,1,1,1,1,1,1,2,2,4,5,1,1,1,1,5,4,1,3,1,1,1,1,4,3,3,3,1,2,3,1,1,1,1,1,1,1,1,2,1,1,1,5,1,3,1,4,3,1,3,1,5,1,1,1,1,3,1,5,1,2,4,1,1,4,1,4,4,2,1,2,1,3,3,1,4,4,1,1,3,4,1,1,1,2,5,2,5,1,1,1,4,1,1,1,1,1,1,3,1,5,1,2,1,1,1,1,1,4,4,1,1,1,5,1,1,5,1,2,1,5,1,1,1,1,1,1,1,1,1,1,1,1,3,2,4,1,1,2,1,1,3,2".split(",")
    #input = "3,4,3,1,2".split(",")

    for i in input:
        if lanternfishes[int(i)] == -1:
           lanternfishes[int(i)] = 1
        else:
            lanternfishes[int(i)] += 1

    for _ in range(1,257):
        lanternfishes = evolution(lanternfishes)
        sum = 0
        for j in lanternfishes:
            if j != -1:
                sum+=j

        print("Day 6, pt 2: " + str(sum) + " executed in " + (str((time.time() - start_time)* 1000)) + " ms")
    
    return sum
    
def evolution(fishes):
    eights = 0
    sixes = 0
    for i in range(0,9):
        if i == 0:
            if fishes[i] != -1:
                sixes=fishes[i]
                eights=fishes[i]
                fishes[i] = -1
        else:
            if fishes[i-1] == -1:
                fishes[i-1] = fishes[i]
                fishes[i] = -1
            else:
                fishes[i-1] = fishes[i-1] + fishes[i] 
                fishes[i] = -1

    if fishes[6] == -1: fishes[6] = sixes
    else: fishes[6] = fishes[6] + sixes

    if fishes[8] == -1: fishes[8] = eights
    else: fishes[8] = fishes[8] + eights

    return fishes


if __name__ == "__main__":
    #part_one()
    part_two()