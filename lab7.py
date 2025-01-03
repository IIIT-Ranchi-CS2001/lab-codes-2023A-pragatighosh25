'''Lab 7 – Data Visualization using matplotlib
Q1 Show party wise seat share for following results of the Assembly Elections 2023 in
Two different pie charts on two different plots. Party with highest percentage should be shown as slightly detached ( show the percentage seat share on each wedge )
Two pie charts as subplots on the same figure object
As a bar chart with party name on X axis and seats won on y axis. Show results of both the states on the same bar plot. Give proper legends
Madhya Pradesh
BJP - Win (163) INC - Win (66) BSP – Win ( 0) Others – Win (1)
Rajasthan
INC - Win (69) BJP- Win (115) BSP- Win (2) Others-Win (13)'''


import matplotlib.pyplot as plt

mp_results = {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1}
rajasthan_results = {"INC": 69, "BJP": 115, "BSP": 2, "Others": 13}

parties = list(mp_results.keys())
mp_seats = list(mp_results.values())
rajasthan_seats = list(rajasthan_results.values())
colors = ["orange", "blue", "green", "grey"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

explode_mp = [0.1 if seats == max(mp_seats) else 0 for seats in mp_seats]
ax1.pie(mp_seats, labels=parties, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode_mp)
ax1.set_title("Madhya Pradesh Assembly Elections 2023")

explode_rajasthan = [0.1 if seats == max(rajasthan_seats) else 0 for seats in rajasthan_seats]
ax2.pie(rajasthan_seats, labels=parties, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode_rajasthan)
ax2.set_title("Rajasthan Assembly Elections 2023")

fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(parties))
ax.bar([i - 0.2 for i in x], mp_seats, width=0.4, label="Madhya Pradesh", color="orange")
ax.bar([i + 0.2 for i in x], rajasthan_seats, width=0.4, label="Rajasthan", color="blue")

ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_xlabel("Parties")
ax.set_ylabel("Seats Won")
ax.set_title("Assembly Elections 2023 Seat Share Comparison")
ax.legend()

plt.tight_layout()

'''
Q2. Write a python script to
Form a list of K random numbers within a limit N where K and N are set by the user. Minimum value of K should be 10.
Define a function (or two functions) to return the composite numbers and prime numbers of this list as two separate lists.
Determine the square of all prime numbers and square root of all composite numbers
Plot both prime numbers Vs their squares and composites Vs their square roots on the same figure object as scatterplots. ( two different subplots on the same figure object)
'''

import random
import math
import matplotlib.pyplot as plt

# Step 1: Generate a list of K random numbers within a limit N
def generate_random_list(K, N):
    return [random.randint(1, N) for _ in range(K)]

# Step 2: Define a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Step 3: Separate prime and composite numbers
def separate_prime_composite(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if num > 1 and not is_prime(num)]
    return primes, composites

# Step 4: Generate the squares of primes and square roots of composites
def calculate_square_and_square_root(primes, composites):
    prime_squares = [num ** 2 for num in primes]
    composite_roots = [math.sqrt(num) for num in composites]
    return prime_squares, composite_roots

# Main code
K = int(input("Enter the number of random numbers (K, minimum 10): "))
N = int(input("Enter the upper limit for random numbers (N): "))

if K < 10:
    print("The minimum value of K should be 10.")
else:
    random_list = generate_random_list(K, N)
    primes, composites = separate_prime_composite(random_list)
    prime_squares, composite_roots = calculate_square_and_square_root(primes, composites)

    # Step 5: Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    ax1.scatter(primes, prime_squares, color='blue')
    ax1.set_title("Prime Numbers vs. Their Squares")
    ax1.set_xlabel("Prime Numbers")
    ax1.set_ylabel("Squares of Primes")

    ax2.scatter(composites, composite_roots, color='green')
    ax2.set_title("Composite Numbers vs. Their Square Roots")
    ax2.set_xlabel("Composite Numbers")
    ax2.set_ylabel("Square Roots of Composites")

    plt.tight_layout()
    plt.show()

plt.show()
