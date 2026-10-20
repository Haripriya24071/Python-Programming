# 2. Find the second-largest value.
nums = [12, 45, 2, 67, 34, 67]
unique_nums = list(set(nums))
unique_nums.sort()
print("Second-largest value:", unique_nums[-2])
