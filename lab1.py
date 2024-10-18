#1. Write a program to find the: Sum,Difference,Product,Integer quotient,Remainder,Fractional quotient of two numbers. Enter the numbers on run time.

def basic_arithmetic_operations():

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    integer_quotient = int(num1 // num2)
    remainder = num1 % num2
    fractional_quotient = num1 / num2

    print("Results:")
    print(f"Sum: {num1} + {num2} = {sum_result}")
    print(f"Difference: {num1} - {num2} = {difference}")
    print(f"Product: {num1} * {num2} = {product}")
    print(f"Integer Quotient: {num1} // {num2} = {integer_quotient}")
    print(f"Remainder: {num1} % {num2} = {remainder}")
    print(f"Fractional Quotient: {num1} / {num2} = {fractional_quotient}")

basic_arithmetic_operations()

#2. Write python program to find
#(a) Area and perimeter of a triangle when all three sides are given. Hint: (Use Heron’s Equation)
#(b) Find all three angles of the triangle given in (a). Display the input data and results in proper format.

import math

def triangle_properties():

    a = float(input("Enter the length of side a: "))
    b = float(input("Enter the length of side b: "))
    c = float(input("Enter the length of side c: "))

    perimeter = a + b + c

    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    angle_C = math.pi - angle_A - angle_B

    angle_A_deg = math.degrees(angle_A)
    angle_B_deg = math.degrees(angle_B)
    angle_C_deg = math.degrees(angle_C)

    print("\nResults:")
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")
    print(f"Angle A: {angle_A_deg:.2f} degrees")
    print(f"Angle B: {angle_B_deg:.2f} degrees")
    print(f"Angle C: {angle_C_deg:.2f} degrees")

triangle_properties()

#3. Write a program to find:
#The equivalent impedance when two impedances Z1 and Z2 are connected in parallel. Display Z1 and Z2 in complex form. 
#Display the real part and imaginary part of the result in separate lines

import cmath

def parallel_impedance():

    real1 = float(input("Enter the real part of Z1: "))
    imag1 = float(input("Enter the imaginary part of Z1: "))
    real2 = float(input("Enter the real part of Z2: "))
    imag2 = float(input("Enter the imaginary part of Z2: "))

    Z1 = complex(real1, imag1)
    Z2 = complex(real2, imag2)
    print(f"Z1: {Z1}")
    print(f"Z2: {Z2}")

    Z_eq = 1 / (1 / Z1 + 1 / Z2)
    real_part = Z_eq.real
    imag_part = Z_eq.imag

    print(f"Equivalent Impedance: {Z_eq}")
    print(f"Real Part: {real_part}")
    print(f"Imaginary Part: {imag_part}")

parallel_impedance()
