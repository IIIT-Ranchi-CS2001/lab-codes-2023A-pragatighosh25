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

#Task 4: Create a program that manages employee salaries in a company using a dictionary. The dictionary should contain at least 5 employees, with their names as keys and their respective salaries as values [take user input data]. Implement a sorting algorithm to arrange the employees in descending order based on their salaries without using any built-in sorting functions, and display the sorted list along with their salaries and rank (highest salary first and so on).
def get_employee_data():
    employees = {}
    for i in range(5):
        name = input(f"Enter the name of employee {i+1}: ")
        salary = int(input(f"Enter the salary of {name}: "))
        employees[name] = salary
    return employees

def sort_employees_by_salary(employees):
    employee_list = list(employees.items())
    
    for i in range(len(employee_list) - 1):
        for j in range(len(employee_list) - 1 - i):
            if employee_list[j][1] < employee_list[j + 1][1]:
                employee_list[j], employee_list[j + 1] = employee_list[j + 1], employee_list[j]
    
    return employee_list

def display_employees(sorted_employees):
    print("\nEmployee Ranking by Salary (Highest first):\n")
    for rank, (name, salary) in enumerate(sorted_employees, start=1):
        print(f"{rank}. {name}: Rs. {salary}")

def main():
    employees = get_employee_data()
    sorted_employees = sort_employees_by_salary(employees)
    display_employees(sorted_employees)

if __name__ == "__main__":
    main()

#task5: 1. Finding the Equation of a Line Given Two Points
x1, y1 = [int(i) for i in input("Enter x1 and y1 separated by space: ").split()]
x2, y2 = [int(i) for i in input("Enter x2 and y2 separated by space: ").split()]

if y1 == y2:
    print(f"The equation of the line is x = {x1}")
else:
    slope = (x1 - x2) / (y1 - y2)
    print(f"The equation of the line is: (x - {x1}) = {slope} (y - {y1})")

#task 6: Counting the Number of Each Character in a String Using a Dictionary

s = input("Enter a string: ")
char_count = {char: s.count(char) for char in s}
print(char_count)

#task 7: Constructing a List of Tuples from Three Lists: Without using zip():

customer_names = [input(f"Enter name of customer {i+1}: ") for i in range(3)]
customer_ids = [int(input(f"Enter ID of customer {i+1}: ")) for i in range(3)]
shopping_points = [int(input(f"Enter shopping points of customer {i+1}: ")) for i in range(3)]

customer_info = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(3)]
print("List of tuples without zip:", customer_info)

#Using zip():

customer_info_zip = list(zip(customer_names, customer_ids, shopping_points))
print("List of tuples with zip:", customer_info_zip)

#task8: Sorting the List of Tuples: Without using sorted():

for i in range(len(customer_info) - 1):
    for j in range(len(customer_info) - 1 - i):
        if customer_info[j][1] > customer_info[j + 1][1]:
            customer_info[j], customer_info[j + 1] = customer_info[j + 1], customer_info[j]

print("Sorted list of tuples without sorted():", customer_info)

#Using sorted():

sorted_customers = sorted(customer_info_zip, key=lambda x: x[1])
print("Sorted list of tuples with sorted():", sorted_customers)






