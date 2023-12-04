from utils import readInput

inputList = readInput("input.txt")

## Part 1
def part1(inputList):
    sum = 0
    for line in inputList:
        first = -1
        for char in line:
            if char.isnumeric():
                if first == -1:
                    first = char
                    last = char
                else:
                    last = char
        if first == -1:
            continue
        sum += int(first + last)
    return sum

## Part 2
def part2(inputList):
    rosetta = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    newList = []
    for line in inputList:
        for key in rosetta:
            line = line.replace(key, rosetta[key])
        newList.append(line)
    return part1(newList)

if __name__ == "__main__":
    print("Part 1: ", part1(inputList))
    print("Part 2: ", part2(inputList))