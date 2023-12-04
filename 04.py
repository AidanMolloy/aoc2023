from utils import readInput

inputList = readInput("input.txt")

def findMatches(card):
  winning_nums, your_nums = card.split(':')[1].split('|')
  return len(set(filter(None, winning_nums.split(' '))) & set(filter(None, your_nums.split(' '))))

## Part 1
def calcScore(matches):
  score = 0
  while matches > 0:
    score = 1 if score == 0 else score * 2
    matches -= 1
  return score

def part1(inputList):
  return sum([calcScore(findMatches(card)) for card in inputList])

## Part 2
def part2(inputList):
  scratchcards = [1] * len(inputList)
  for card_idx in range(len(inputList)):
    matches = findMatches(inputList[card_idx])
    for i in range(1, matches+1):
      scratchcards[card_idx+i] += scratchcards[card_idx]

  return sum(scratchcards)

if __name__ == "__main__":
    print("Part 1: ", part1(inputList))
    print("Part 2: ", part2(inputList))