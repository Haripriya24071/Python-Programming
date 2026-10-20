# 1. Course Enrollment Set Operations (Lab Test)
course_1 = {101, 102, 103, 104}
course_2 = {103, 104, 105, 106}
course_3 = {101, 104, 107, 108}

print("Course 1 roll numbers:", course_1)
print("Course 2 roll numbers:", course_2)
print("Course 3 roll numbers:", course_3)
print("-" * 45)

all_three = course_1 & course_2 & course_3
print("Students in all three courses:", all_three)

at_least_one = course_1 | course_2 | course_3
print("Students in at least one course:", at_least_one)

c1_not_c2 = course_1 - course_2
print("Students in Course 1 but not Course 2:", c1_not_c2)

exactly_two = ((course_1 & course_2) | (course_2 & course_3) | (course_1 & course_3)) - all_three
print("Students taking exactly two courses:", exactly_two)
print("Number of students taking exactly two courses:", len(exactly_two))

exactly_one = (course_1 - course_2 - course_3) | (course_2 - course_1 - course_3) | (course_3 - course_1 - course_2)
print("Students taking exactly one course:", exactly_one)
