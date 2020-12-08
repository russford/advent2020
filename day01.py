def part1 (nums):
    for n in nums:
        if 2020-n in nums:
            print (n*(2020-n))
            break

def part2 (nums):
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            if 2020-nums[i]-nums[j] in nums[j:]:
                print (nums[i]*nums[j]*(2020-nums[i]-nums[j]))


with open ("day01.txt", "r") as f:
    nums = sorted([int(a) for a in f.readlines()])

part1 (nums)
part2 (nums)

