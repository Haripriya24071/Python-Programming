# 2. Given a list of strings, extract strings with length greater than 3 and convert them into uppercase.

a = ["cat", "apple", "dog", "banana", "pen"]

b = list(filter(lambda x: len(x) > 3, a))
c = list(map(lambda x: x.upper(), b))

print("Strings with length greater than 3:", b)
print("Uppercase strings:", c)

