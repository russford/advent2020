def do_move_part1(str):
    ins_cup = str[0]
    three_cups = str[1:4]
    other_cups = str[4:]

    # print (ins_cup, three_cups, other_cups)

    for i in range(1,1000000):
        if (ins_cup-i-1) % 1000000 + 1 in other_cups:
            break
    ins_index = other_cups.index((ins_cup-i-1) % 1000000 + 1)

    return other_cups[:ins_index+1] + three_cups + other_cups[ins_index+1:] + [ins_cup]

def part1 (cups):
    for i in range(100):
        # print (", ".join(str(c) for c in cups))
        one = cups.index(1)
        cups = do_move(cups)
    i = cups.index(1)
    print("".join(str(c) for c in cups[i + 1:] + cups[:i]))

def load_cups (cups, total=0):
    n = len (cups)+1
    if total: n = total+1
    arr = [0] * n
    for i, c in enumerate(cups[:-1]):
        arr[c] = cups[i+1]
    if total:
        arr[cups[-1]] = len(cups) + 1
        for i in range(len(cups)+1, total):
            arr[i] = i+1
        arr[i+1] = cups[0]
    else:
        arr[cups[-1]] = cups[0]
    return arr

def print_cups (cups, first):
    s = ""
    n = first
    while True:
        s += str(n) +","
        n = cups[n]
        if n == first: return s

def do_move (cups, curr_cup):
    p0 = cups[curr_cup]
    p1 = cups[p0]
    p2 = cups[p1]
    next = cups[p2]
    dest = (curr_cup - 2) % (len(cups)-1) + 1
    while dest in [p0, p1, p2]:
        dest = (dest - 2) % (len(cups)-1) + 1
        if dest == 0:
            pass
    cups[curr_cup] = next
    cups[p2] = cups[dest]
    cups[dest] = p0
    return next



def print_ro1 (n):
    while n.data != 1:
        n = n.next
    print(n.data, n.next.data, n.next.next.data)
    print(n.next.data * n.next.next.data)

def part2 (cups, n1, n2):
    # succ = load_cups(cups)
    succ = load_cups(cups,n1)
    n = cups[0]
    for i in range(n2):
        # print (print_cups(succ, n))
        n = do_move(succ, n)
    print (succ[1], succ[succ[1]], succ[1]*succ[succ[1]])


cups_a = [3, 8, 9, 1, 2, 5, 4, 6, 7]
cups = [3, 6, 4, 2, 9, 7, 5, 8, 1]

# part1 (cups)
# part2(cups_a, 0, 10)
part2 (cups, 1000000, 10000000)





