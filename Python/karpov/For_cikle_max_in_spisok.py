# ссылка на задачу https://lab.karpov.courses/learning/243/module/2453/lesson/23855/68546/331884/
nums = [9, 9, 99, -23]
nums.sort()
min_diff = float("inf")
min_diff1 = float("-inf")
d = len(nums)
a = 0
for j in nums:
    for i in nums:
        if nums.index(j) != nums.index(i):
            z = abs(j - i)

        else:
            continue
        if z <= min_diff:
            min_diff = z
            a = abs(j + i)
            if a > min_diff1:
                min_diff1 = a
                result = [j, i]
print(result)
