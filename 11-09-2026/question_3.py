# 3. Count how many times a particular number occurs in a list
nums = [1, 2, 3, 2, 4, 2, 5]
target = 2
count = 0
for n in nums:
    if n == target:
        count += 1
print("Count of", target, "is:", count)
