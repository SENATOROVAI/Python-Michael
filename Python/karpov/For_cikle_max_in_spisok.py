nums = [1, 2, 3, 4]
nums.sort()
min_diff = float("inf")
min_diff1 = float("-inf")
d = len(nums)
a = 0
for j in nums:
    for i in nums:
        if j != i:
            z = abs(j - i)
        elif nums.count(i) >= 2:
            result = [i, i]
            break
        else:
            continue
        if z <= min_diff:
            min_diff = z
            a = abs(j + i)
            if a > min_diff1:
                min_diff1 = a
                result = [j, i]
print(result)
