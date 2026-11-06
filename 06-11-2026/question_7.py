# 7. Write a program to extract numbers that are perfect squares from a given list.

a = [1, 4, 6, 9, 12, 16, 20, 25, 30]

b = list(filter(lambda x: int(x ** 0.5) ** 2 == x, a))

print("Perfect square numbers:", b)

