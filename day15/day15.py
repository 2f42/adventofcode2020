def read_input(s="6,19,0,5,7,13,1"):
    out = [int(i) for i in s.split(",")]
    return out

def read_nums(nums, r=2020):
    nums_spoken = {}
    last_spoken = 0
    next_spoken = 0
    for i in range(r):
        last_spoken = next_spoken
        if nums:
            last_spoken = nums.pop(0)
        if last_spoken in nums_spoken:
            next_spoken = i - nums_spoken[last_spoken]
        else:
            next_spoken = 0
        nums_spoken[last_spoken] = i
    return last_spoken

print(read_nums(read_input(), 30000000))
