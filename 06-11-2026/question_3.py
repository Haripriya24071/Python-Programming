# 3. Write a program to extract numbers divisible by 2 or 3 and calculate their squares.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(lambda x: x % 2 == 0 or x % 3 == 0, a))
c = list(map(lambda x: x ** 2, b))

print("Numbers divisible by 2 or 3:", b)
print("Squares:", c)

