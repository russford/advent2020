from collections import deque

def score_hand (hand):
    return sum([(len(hand)-i)*c for i, c in enumerate(hand)])

with open ("day22.txt", "r") as f:
    data = f.read().split("\n\n")
hands = [list(map(int, d.split("\n")[1:])) for d in data]

p1 = deque(hands[0])
p2 = deque(hands[1])

while p1 and p2:
    c1 = p1.popleft()
    c2 = p2.popleft()
    if c1 > c2:
        p1.append(c1)
        p1.append(c2)
    else:
        p2.append(c2)
        p2.append(c1)

print (score_hand(p1 or p2))




