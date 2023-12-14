from utils import runner
from math import lcm

def readMap(inputList):
  node_map = {}
  line_idx = 2
  while line_idx < len(inputList):
    line = inputList[line_idx]
    left, right = line.split('=')[1].replace(' ', '').replace('(', '').replace(')', '').split(',')
    node_map[line.split('=')[0].strip()] = (left, right)
    line_idx += 1
  return inputList[0], node_map

def findSteps(current_node, instructions, node_map, target_node):
  steps = 0
  while(True):
    for instruction in instructions:
      if current_node.endswith(target_node):
        return steps
      current_node = node_map[current_node][0 if instruction == 'L' else 1]
      steps += 1

## Part 1
def part1(inputList):
  instructions, node_map = readMap(inputList)
  return findSteps("AAA", instructions, node_map, 'ZZZ')

## Part 2
def part2(inputList):
  instructions, node_map = readMap(inputList)
  starting_nodes = [node for node in node_map if node.endswith('A')]
  steps_required = []

  for node in starting_nodes:
    steps_required.append(findSteps(node, instructions, node_map, 'Z'))
  
  return lcm(*steps_required)

if __name__ == "__main__":
    runner(part1, part2, sample2="sample2.txt")