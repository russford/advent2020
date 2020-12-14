with open("day09.txt", "r") as f:
    data = [int(a) for a in f.read().splitlines()]


def find_missing (arr, n):
    for i in range(n, len(data)):
        # print (i, data[i], data[i-n:i])
        if not any([data[i] - data[i - j] in data[i - n:i] and data[i - j] != 2 * data[i] for j in range(1, n+1)]):
            return data[i]


def find_contiguous (arr, n):
    for i in range(len(arr)-1):
        total = arr[i]
        j = 1
        while total < n and i+j < len(arr):
            total += arr[i+j]
            j += 1
        if total == n and j > 1:
            return min(arr[i:i+j])+max(arr[i:i+j])


def find_sliding (arr, n):
    cumsum = [sum(arr[:i]) for i in range(len(arr))]
    i, j = 0, 1
    mode = 0
    while True:
        if cumsum[j] - cumsum[i] == n or i == len(arr)-2:
            break
        if mode == 1:
            i += 1
            if j-1 == 1 or cumsum[j]-cumsum[i] < n:
                mode = 0
        else:
            j += 1
            if j > len(arr) or cumsum[j]-cumsum[i] > n:
                mode = 1
    print (i, j, cumsum[j]-cumsum[i])
    return max(arr[i:j]) + min(arr[i:j])




test_data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

# data = [int(a) for a in test_data.split('\n')]
# print (data)

a = find_missing(data, 25)
print (a, find_sliding(data, a))



