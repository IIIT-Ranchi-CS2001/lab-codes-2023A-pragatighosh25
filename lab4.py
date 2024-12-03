#Task 1: Count Palindrome Words in a Sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
palindrome_count = sum(1 for word in words if word.lower() == word[::-1].lower())
print("Number of palindrome words:", palindrome_count)

#task2: Mean, Median, and Mode of a List

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(numbers)

# Mean
mean = sum(numbers) / n

# Median
sorted_numbers = sorted(numbers)
if n % 2 == 0:
    median = (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
else:
    median = sorted_numbers[n//2]

# Mode
mode = max(set(numbers), key=numbers.count)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

#Task 3: Create Course Code and Name Lists

course_codes = ["CS1001", "CS1002", "CS1003"]
course_names = ["Python", "Data Structures", "Algorithms"]

course_list = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
print("Course List:", course_list)

#Set Operations for Artists

singers = {"akshay", "barsha", "catto"}
dancers = {"barsha", "diya", "kanika"}

# All artists
all_artists = singers | dancers

# All-rounders (singers and dancers)
all_rounders = singers & dancers

# Dancers but not singers
dancers_not_singers = dancers - singers

# Singers but not dancers
singers_not_dancers = singers - dancers

# Combined set of dancers not singers and singers not dancers
combined = dancers_not_singers | singers_not_dancers

print("All Artists:", all_artists)
print("All-rounders:", all_rounders)
print("Dancers but not Singers:", dancers_not_singers)
print("Singers but not Dancers:", singers_not_dancers)
print("Combined Set:", combined)
