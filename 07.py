from utils import runner

## Part 1
p1_card_vals = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

def part1(inputList):
  hands = []
  for line in inputList:
    cards, bid = line.split()
    hand = [0] * 13
    new_cards = []
    for card in cards:
      hand[p1_card_vals[card]] += 1
      new_cards.append(p1_card_vals[card])
    val = max(hand)
    hand.remove(val)
    if(max(hand) == 2):
       val += 0.5
    hands.append((val, new_cards, int(bid)))
  return sum([hand[2] * (i+1) for i, hand in enumerate(sorted(hands))])

## Part 2
p2_card_vals = {'A': 12, 'K': 11, 'Q': 10, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}

def part2(inputList):
  hands = []
  for line in inputList:
    cards, bid = line.split()
    hand = [0] * 13
    new_cards = []
    for card in cards:
      hand[p2_card_vals[card]] += 1
      new_cards.append(p2_card_vals[card])
    jokers = hand[0]
    del hand[0]
    val = max(hand)
    hand.remove(val)
    if(max(hand) == 2):
       val += 0.5
    val += jokers
    hands.append((val, new_cards, int(bid)))
  return sum([hand[2] * (i+1) for i, hand in enumerate(sorted(hands))])

if __name__ == "__main__":
    runner(part1, part2)