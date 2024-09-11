#1. Write a python script to find the squares of first n natural numbers. Display both the number and the square as shown below. Use while loop


def print_squares(n):
    print("Number\tSquare")
    num = 1
    while num <= n:
        square = num ** 2
        print(num,"\t",square)
        num += 1

n = int(input("Enter the value of n: "))
print_squares(n)

#2.Write a python script to find the sum of the digits of the given number using a while loop. Display the number and the sum.


def sum_of_digits(number):
    number = abs(number)
    digit_sum = 0
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    return digit_sum

number = int(input("Enter a number: "))
result = sum_of_digits(number)


print(f"Number: {number}")
print(f"Sum of digits: {result}")


#3. Write a python script to print the first n terms of the Fibonacci series using while loop


def print_fibonacci(n):
    a, b = 0, 1
    count = 0
    print("Fibonacci Series:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()

n = int(input("Enter the number of terms: "))
print_fibonacci(n)


#4. Write a python script to print the multiplication table of a given number up to the specified limit using a for loop.

def multiplication_table(num):
    print("Multiplication table for",num)
    for i in range(1,11):
        product = num * i
        print(number,"x",i,"=",product)

num = int(input("Enter the number for the multiplication table: "))
multiplication_table(num)

#5. Write a python script to check whether all the characters present in a string are alphanumeric (uppercase letters, lowercase letters or digits) using for  with else. Print True if all characters are alphanumeric. Otherwise print False.

def is_alphanumeric(s):
    for char in s:
        if not char.isalnum():
            print(False)
            break
    else:
        print(True)


string = "Hello123"
is_alphanumeric(string)

#6. Write a python script to find the number of occurrences of a particular character present in the given string using a loop. (Don’t use string methods).
def count_char_occurrences(s, target_char):
    count = 0
    for char in s:
        if char == target_char:
            count += 1
    return count

input_string = "hello world"
target_character = 'o'
result = count_char_occurrences(input_string, target_character)
print("The character",target_character, "appears",result,"result times in the string.")

