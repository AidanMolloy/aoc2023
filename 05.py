from utils import runner

def parse_almanac(inputList, reverse=False):
  almanac = {"seeds": list(map(int, inputList[0].split("seeds: ")[1].split()))}
  line_idx = 2
  source = destination = None
  while len(inputList) > line_idx:
    line = inputList[line_idx]
    if line.endswith("map:"):
      source, destination = line.split(" map:")[0].strip().split("-")[::2]
      if reverse:
        source, destination = destination, source
    elif line != "":
      if source in almanac:
        almanac[source].append(tuple(map(int, line.split())))
      else:
        almanac[source] = [destination, tuple(map(int, line.split()))]
    line_idx += 1
  for key in almanac:
    if key != "seeds":
      almanac[key] = almanac[key][0], sorted(almanac[key][1:], key=lambda x: x[0 if reverse else 1])
  return almanac

def find_matching_value(value, pairs, reversed=False):
  low = mid = 0
  high = len(pairs) - 1
  source = 0 if reversed else 1
  target = 1 if reversed else 0
  while low <= high:
    mid = (high + low) // 2
    if pairs[mid][source] <= value <= pairs[mid][source]+pairs[mid][2]:
      return value - pairs[mid][source] + pairs[mid][target]
    elif pairs[mid][source] < value:
      low = mid + 1
    elif pairs[mid][source]+pairs[mid][2] > value:
      high = mid - 1
    else:
      return value
  return value

def sourceToTarget(value, source_type, target_type, almanac, reversed=False):
  while(source_type != target_type):
    value = find_matching_value(value, almanac[source_type][1], reversed=reversed)
    source_type = almanac[source_type][0]
  return value

## Part 1
def part1(inputList):
  min_location = float('inf')
  almanac = parse_almanac(inputList)
  for seed in almanac["seeds"]:
    location = sourceToTarget(seed, "seed", "location", almanac)
    if location < min_location:
      min_location = location
  return min_location

## Part 2
def part2(inputList):
  almanac = parse_almanac(inputList, reverse=True)
  seed_ranges = [(almanac["seeds"][start_idx], almanac["seeds"][start_idx]+almanac["seeds"][start_idx+1]) for start_idx in range(0, len(almanac["seeds"]), 2)]
  location = 0
  while(True):
    seed = sourceToTarget(location, "location", "seed", almanac, reversed=True)
    for seed_range in seed_ranges:
      if seed_range[0] <= seed <= seed_range[1]:
        return location
    location += 1

if __name__ == "__main__":
    runner(part1, part2)