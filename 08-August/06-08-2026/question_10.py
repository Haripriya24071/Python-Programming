# 10. Fibonacci Series
n = 10
a, b = 0, 1
print(f"First {n} terms of Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
