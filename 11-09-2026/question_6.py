# 6. Common Elements of Two Tuples
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
common = tuple(set(t1) & set(t2))
print("Tuple 1:", t1)
print("Tuple 2:", t2)
print("Common elements:", common)
