def read_input(fname="input.txt"):
    nums = []
    with open(fname) as f:
        for line in f.readlines():
            new = int(line.strip())
            nums.append(new)
    return nums

def find_invalid(nums):
    for n in range(25,len(nums)):
        found = False
        for i in nums[n-25:n]:
            for j in nums[n-25:n]:
                if i == j:
                    continue
                if i + j == nums[n]:
                    found = True
                    break
            if found:
                break
        if not found:
            return nums[n]

def find_weakness(nums, target):
    cont_set = []
    for n in nums:
        cont_set.append(n)
        if len(cont_set) <= 1:
            continue
        if sum(cont_set) == target:
            return min(cont_set) + max(cont_set)
        while sum(cont_set) > target:
            cont_set.pop(0)

nums = read_input()
invalid = find_invalid(nums)
print("part1:\t", invalid)
print("part2:\t", find_weakness(nums, invalid))
