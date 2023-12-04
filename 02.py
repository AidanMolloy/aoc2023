from utils import readInput

inputList = readInput("input.txt")

## Part 1
def part1(inputList):
    maxColors = {"red": 12, "green": 13, "blue": 14}
    sum = 0

    for game in inputList:
        game_info, game = game.split(':')
        game_id = int(game_info.split()[1])
        possible = True
        for subgame in game.split(';'):
            colorTotals = {"red": 0, "green": 0, "blue": 0}
            for color in subgame.split(','):
                num, name = color.split()
                colorTotals[name] += int(num)
            for color in colorTotals:
                if colorTotals[color] > maxColors[color]:
                    possible = False
                    break
        if possible:
            sum += game_id
    return sum

## Part 2
def part2(inputList):
    sum = 0
    for game in inputList:
        minColors = {"red": 0, "green": 0, "blue": 0}
        for subgame in game.split(':')[1].split(';'):
            colorTotals = {"red": 0, "green": 0, "blue": 0}
            for color in subgame.split(','):
                num, name = color.split()
                colorTotals[name] += int(num)
            for color in colorTotals:
                if colorTotals[color] > minColors[color]:
                    minColors[color] = colorTotals[color]
        res = 1
        for i in list(minColors.values()):
            res *= i
        sum += res
    return sum

if __name__ == "__main__":
    print("Part 1: ", part1(inputList))
    print("Part 2: ", part2(inputList))