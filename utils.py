import sys
from pathlib import Path

def readInput(filename):
  inputList = []
  day = sys.argv[0].strip(".py")
  with open(Path(__file__).resolve().parent / day / filename) as file:
    while line := file.readline():
      inputList.append(line.rstrip())
  return inputList