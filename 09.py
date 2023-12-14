from utils import runner

def nextVal(graph, prev=False):
  row = -1
  while (graph[row][-1] - graph[row][-2] != 0):
    row += 1
    graph.append([graph[row][i+1] - graph[row][i] for i in range(0, len(graph[row])-1)])

  graph[-1].append(0)
  while row > 0:
    graph[row].append(graph[row][0] - graph[row+1][-1] if prev else graph[row][-1] + graph[row+1][-1])
    row -= 1
  return graph[row][0] - graph[row+1][-1] if prev else graph[row][-1] + graph[row+1][-1]

## Part 1
def part1(inputList):
  return sum([nextVal([list(map(int, line.split()))]) for line in inputList])

## Part 2
def part2(inputList):
  return sum([nextVal([list(map(int, line.split()))], prev=True) for line in inputList])

if __name__ == "__main__":
    runner(part1, part2)