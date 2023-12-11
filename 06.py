from utils import runner

## Part 1
def part1(inputList):
  sum = 1
  time = list(map(int, inputList[0].split(':')[1].strip().split()))
  distance = list(map(int, inputList[1].split(':')[1].strip().split()))
  for i in range(0, len(time)):
    ways = 0
    for j in range(0, time[i]):
      if (time[i] - j) * j > distance[i]:
        ways += 1
    sum *= ways
  return sum

## Part 2
def part2(inputList):
  time = int(inputList[0].split(':')[1].strip().replace(' ', ''))
  distance = int(inputList[1].split(':')[1].strip().replace(' ', ''))
  ways = time
  i = 0
  while((time - i) * i < distance):
    ways -= 1
    i += 1
  j = time
  while((time - j) * j < distance):
    ways -= 1
    j -= 1
  return ways

if __name__ == "__main__":
    runner(part1, part2)