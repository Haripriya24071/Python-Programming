# 1. Given a list of integers, extract even numbers, calculate their squares, and then extract squares greater than 100.

a = list(map(int, input("Enter numbers: ").split()))

b = list(filter(lambda x: x % 2 == 0, a))
c = list(map(lambda x: x ** 2, b))
d = list(filter(lambda x: x > 100, c))

print("Even numbers:", b)
print("Squares:", c)
print("Squares greater than 100:", d)
