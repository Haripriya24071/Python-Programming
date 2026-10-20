# 1. Course enrollment set operations
# Accept roll numbers enrolled in three courses as sets. Display students in all three courses, students in at least one course, students in exactly one course, students in course one but not course two, and the number of students taking exactly two courses.

a = set()
b = set()
c = set()

n = input("Enter course 1 roll numbers: ").split()
for i in n:
    a.add(int(i))

n = input("Enter course 2 roll numbers: ").split()
for i in n:
    b.add(int(i))

n = input("Enter course 3 roll numbers: ").split()
for i in n:
    c.add(int(i))

print("All three:", a & b & c)
print("At least one:", a | b | c)
print("Course 1 not course 2:", a - b)

x = (a & b) | (b & c) | (a & c)
x = x - (a & b & c)
print("Exactly two:", len(x))

x = (a - b - c) | (b - a - c) | (c - a - b)
print("Exactly one:", x)
