# 4. Given a list of integers, add 10 to every element and then extract elements greater than 30.

a = [10, 15, 20, 25, 30]

b = list(map(lambda x: x + 10, a))
c = list(filter(lambda x: x > 30, b))

print("After adding 10:", b)
print("Elements greater than 30:", c)

