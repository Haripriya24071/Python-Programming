# 5. Fibonacci Series
n = 10
a, b = 0, 1
print(f"Fibonacci series (first {n} terms):")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
