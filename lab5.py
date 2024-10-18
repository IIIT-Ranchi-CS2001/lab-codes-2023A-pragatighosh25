#Task 1: Euclidean Distance Between Two Points

import math
point1 = (1, 2, 3)
point2 = (4, 5, 6)

distance = math.sqrt(sum((p2 - p1) ** 2 for p1, p2 in zip(point1, point2)))
print("Euclidean distance between the points:", distance)

#Task 2: Creating and Sorting a List of Student Details

names = ["akshay", "Barsha", "catto"]
roll_nos = [101, 102, 103]
marks = [85, 90, 78]

student_details = list(zip(names, roll_nos, marks))
sorted_students = sorted(student_details, key=lambda x: x[2])
print("Sorted student details by marks:", sorted_students)

#Task 3: Redo Without Using zip and sorted

manual = []
for i in range(len(names)):
    manual.append((names[i], roll_nos[i], marks[i]))

for i in range(len(manual)):
    for j in range(0, len(manual)-i-1):
        if manual[j][2] > manual[j+1][2]:
            manual[j], manual[j+1] = manual[j+1], manual[j]

print("Sorted student details by marks (manual):", manual)

#Task 4: Count Each Letter in a String Using a Dictionary

input_string = input("Enter a string: ")

letter_count = {}
for letter in input_string:
    if letter.isalpha():  
        letter_count[letter] = letter_count.get(letter, 0) + 1

print("Count of each letter:", letter_count)
