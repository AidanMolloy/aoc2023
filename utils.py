import sys
from pathlib import Path
from time import perf_counter

def readInput(filename):
  inputList = []
  day = sys.argv[0].strip(".py")
  with open(Path(__file__).resolve().parent / day / filename) as file:
    while line := file.readline():
      inputList.append(line.rstrip())
  return inputList

def runner(part1, part2):
  print("----------------------------------------------")
  print(f"Part 1 - Sample answer: {part1(readInput('sample.txt'))}")
  time_start = perf_counter()
  result = part1(readInput('input.txt'))
  time_stop = perf_counter()
  print(f"Part 1 - Answer:        {result} ({time_stop-time_start:.4f}s)")
  print("----------------------------------------------")
  print(f"Part 2 - Sample answer: {part2(readInput('sample.txt'))}")
  time_start = perf_counter()
  result = part2(readInput('input.txt'))
  time_stop = perf_counter()
  print(f"Part 2 - Answer:        {result} ({time_stop-time_start:.4f}s)")
  print("----------------------------------------------")