from utils import runner

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)]

def readNum(inputList, row, col):
    while col-1 >= 0 and inputList[row][col-1].isnumeric():
        col -= 1
    num = ""
    while col < len(inputList[row]) and inputList[row][col].isnumeric():
        num += inputList[row][col]
        col += 1
    return int(num), (row, col)

## Part 1
def isPart(row, col, newCol, inputList):
    for i in range(col, newCol):
        for dx, dy in adjacency:
            if 0 <= (row + dx) < len(inputList) and 0 <= i + dy < len(inputList[row]):
                if not inputList[row+dx][i+dy].isnumeric() and inputList[row+dx][i+dy] != ".":
                    return True
    return False

def part1(inputList):
    parts = []
    for row in range(len(inputList)):
        col = 0
        while col < len(inputList[row]):
            if inputList[row][col].isnumeric():
                num, (_, newCol) = readNum(inputList, row, col)
                if isPart(row, col, newCol, inputList):
                    parts.append(num)
                col = newCol
            else:
                col += 1

    return sum(parts)

## Part 2
def gearRatio(gear, inputList):
    sum = 0
    numbers = set()
    row, col = gear
    for dx, dy in adjacency:
        if 0 <= (row + dx) < len(inputList) and 0 <= col + dy < len(inputList[row]):
            if inputList[row+dx][col+dy].isnumeric():
                num, numIndex = readNum(inputList, row+dx, col+dy)
                if numIndex not in numbers:
                    numbers.add(numIndex)
                    sum = num if sum == 0 else sum * num
    
    return sum if len(numbers) == 2 else 0

def part2(inputList):
    gears = [(row, col) for row in range(len(inputList)) for col in range(len(inputList[row])) if inputList[row][col] == "*"]
    return sum([gearRatio(gear, inputList) for gear in gears])

if __name__ == "__main__":
    runner(part1, part2)