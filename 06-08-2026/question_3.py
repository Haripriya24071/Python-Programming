# 3. Largest of Three Numbers
a = 15
b = 40
c = 25

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)
