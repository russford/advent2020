input = [0,8,15,2,12,1,4]
test_input = [0,3,6]

def run_game(seq, n):
    indexes = {v:i for i,v in enumerate(seq[:-1])}
    for i in range(len(seq), n):
        last = seq[-1]
        if last in indexes:
            next = i - indexes[last] - 1
        else:
            next = 0
        indexes[last] = i-1
        seq.append(next)
    print(len(indexes))
    return next

print(run_game(input, 2020))
print(run_game(input, 30000000))


