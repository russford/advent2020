from collections import deque

def score_hand (hand):
    print (hand)
    return sum([(len(hand)-i)*c for i, c in enumerate(hand)])

def part1 (hands):
    p1 = hands[0]
    p2 = hands[1]

    while p1 and p2:
        c1 = p1[0]
        c2 = p2[0]
        if c1 > c2:
            p1 = p1[1:] + [c1, c2]
            p2 = p2[1:]
        else:
            p2 = p2[1:] + [c2, c1]
            p1 = p1[1:]

    print (score_hand(p1 or p2))


def recursive_combat (hands, print_score=0):
    p1 = hands[0]
    p2 = hands[1]

    seen_hands = []

    # print ("starting game of recursive combat")
    while p1 and p2:
        # print ()
        # print (p1)
        # print (p2)
        if (p1, p2) in seen_hands:
            # print ("been here before; player 1 wins")
            return 1
        seen_hands.append((p1,p2))

        c1 = p1[0]
        c2 = p2[0]
        if len(p1)-1 < c1 or len(p2)-1 < c2:
            if c1 > c2:
                # print ("p1 wins")
                p1 = p1[1:] + [c1, c2]
                p2 = p2[1:]
            else:
                # print ("p2 wins")
                p2 = p2[1:] + [c2, c1]
                p1 = p1[1:]
        else:
            # print ("recursing...")
            if recursive_combat([p1[1:c1+1], p2[1:c2+1]]) == 1:
                # print ("p1 won the recursion")
                p1 = p1[1:] + [c1, c2]
                p2 = p2[1:]
            else:
                # print ("p2 won the recursion")
                p2 = p2[1:] + [c2, c1]
                p1 = p1[1:]
    if print_score:
        print (score_hand(p1 or p2))
    return 1 if p1 else 0


def part2 (hands):
    p1 = hands[0]
    p2 = hands[1]
    result = recursive_combat([p1, p2], 1)


with open ("day22.txt", "r") as f:
    data = f.read().split("\n\n")
hands = [list(map(int, d.split("\n")[1:])) for d in data]


# hands = [[9,2,6,3,1], [5,8,4,7,10]]

part2(hands)






