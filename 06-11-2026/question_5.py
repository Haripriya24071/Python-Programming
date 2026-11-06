# 5. Write a program to extract negative numbers and convert them into their absolute values.

a = [-5, 10, -8, 20, -3, 6]

b = list(filter(lambda x: x < 0, a))
c = list(map(lambda x: abs(x), b))

print("Negative numbers:", b)
print("Absolute values:", c)

