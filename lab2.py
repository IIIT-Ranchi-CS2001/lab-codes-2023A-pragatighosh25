#1. If the given string S1= “Maha Bharat”, generate the following strings by manipulating S1.
# Original string
S1 = "Maha Bharat"

# a. "mAHA bHARAT"
first_part = S1[:4]
first_part_transformed = first_part[0].lower() + first_part[1:].upper()
second_part = S1[5:]
second_part_transformed = second_part[0].lower() + second_part[1:].upper()
S2 = first_part_transformed + " " + second_part_transformed
print(S2)

# b. "Bharat"
S3 = S1[5:]
print(S3)

# c. "BharatBharatBharat"
S4 = S3 * 3
print(S4)

# d. "Mera Bharat"
S5 = "Mera " + S3
print(S5)

# e. "Mera Bharat Mahan"
S6 = S5 + " Mahan"
print(S6)

'''2.For the given string S=”Ba Ba Black Sheep”, determine the following using built in functions:
1.The length of the string S
2.The first occurrence of the letter ‘e’
3.The total number of occurrences of ‘a’
4.Generate “Ta Ta Black Sheep”'''

S = "Ba Ba Black Sheep"

# a. Length of the string S
length_of_S = len(S)

print("Length of S:", length_of_S)

# b. First occurrence of the letter 'e'
first_occurrence_of_e = S.find('e')
print("First occurrence of 'e':", first_occurrence_of_e)

# c. Total number of occurrences of 'a'
total_occurrences_of_a = S.count('a')
print("Total number of occurrences of 'a':", total_occurrences_of_a)

# d. Generate "Ta Ta Black Sheep", Replace 'B' with 'T' in the original string
modified_string = S.replace('B', 'T')
print("Modified string:", modified_string)

#3. Write a python script to enter any string at run time and check whether it is a palindrome or not.
string = input("Enter a string: ")
new_string = ''.join(string.lower().split())
if new_string == new_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4. Enter the following details of a student at run time: - Name, Roll number and marks secured for Mathematics Examination out of 100. Write a python script to display student details as shown: Name,Roll Number,Marks,Grade Point,Remark.

def grade_remark(marks):
    if marks >= 90:
        return 10, "OUTSTANDING"
    elif 80 <= marks < 90:
        return 9, "VERY GOOD"
    elif 70 <= marks < 80:
        return 8, "GOOD"
    elif 60 <= marks < 70:
        return 7, "AVERAGE"
    elif 50 <= marks < 60:
        return 6, "PASS"
    else:
        return 0, "FAIL"

name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")
marks = int(input("Enter the marks secured in Mathematics (out of 100): "))

grade_point, remark = grade_remark(marks)
print("\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"Marks: {marks}")
print(f"Grade Point: {grade_point}")
print(f"Remark: {remark}")

#5. Write a program to find the roots of a quadratic equation when the coefficients a, b and c are given ( assume that a, b and c are integers)

import math

def find_roots(a, b, c):
    dis = b**2 - 4*a*c
    if dis > 0:
        root1 = (-b + math.sqrt(dis)) / (2 * a)
        root2 = (-b - math.sqrt(dis)) / (2 * a)
        return (root1, root2)
    
    elif dis == 0:
        root = -b / (2 * a)
        return (root, root)
    
    else:
        real_part = -b / (2 * a)
        img_part = math.sqrt(-dis) / (2 * a)
        return (f"{real_part} + {img_part}i", f"{real_part} - {img_part}i")

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

roots = find_roots(a, b, c)

print("The roots of the equation are:")
print(f"Root 1: {roots[0]}")
print(f"Root 2: {roots[1]}")
