'''task1:Define a function my_zip() that can form a list of tuples by iterating the following customer details:-
‘customer Name, customer ID , shopping points’ and based on the keyword parameter ‘strct’: If strct =
True, zipping shall be done only if all lists are of equal length.
If strct = False, zipping can be done by taking the minimum length of the iterable.'''

def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("All lists must be of equal length for strict zipping.")
    else:
        min_len = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_len)]

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [102, 101, 103]
shopping_points = [500, 400, 600]

try:
    zipped_data_strict = my_zip(customer_names, customer_ids, shopping_points, strct=True)
    print("Strict zipped data:", zipped_data_strict)
except ValueError as e:
    print(e)
    
zipped_data_non_strict = my_zip(customer_names, customer_ids, shopping_points, strct=False)
print("Non-strict zipped data:", zipped_data_non_strict)

'''task2: Define a function my_sort() to sort the list of tuples created using my_zip function in the last question.
The function must have two types of arguments- the list that carry the data, the key that determines the argument of sorting:
[Usage of built-in function sorted() is a punishable offense]
Key = 0: sorting based on customer name in ascending order
Key = 1: sorting based on Customer ID
Key = 2: sorting based on shopping points'''

def my_sort(data, key=0):
    n = len(data)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    
    return data

customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [102, 101, 103]
shopping_points = [500, 400, 600]

zipped_data = my_zip(customer_names, customer_ids, shopping_points, strct=True)

sorted_by_name = my_sort(zipped_data, key=0)
print("Sorted by customer name:", sorted_by_name)

sorted_by_id = my_sort(zipped_data, key=1)
print("Sorted by customer ID:", sorted_by_id)

sorted_by_points = my_sort(zipped_data, key=2)
print("Sorted by shopping points:", sorted_by_points)

'''task 3:Write program to define a function my_max() to complete the following tasks: [Usage of built-in function max() is strictly prohibited]
If a list of integers is passed as the input argument, the function shall return maximum value present in the list
If a set is passed, maximum value present in the list
If a tuple is passed, maximum value present in the tuple
Hint: Pass the container type unpacked using'''

def my_max(*container):
    if len(container) == 0:
        raise ValueError("The container is empty.")
    
    max_value = container[0]

    for value in container:
        if value > max_value:
            max_value = value
    
    return max_value

my_list = [1, 4, 9, 7, 2]
my_set = {11, 22, 5, 8}
my_tuple = (3, 6, 2, 8, 1)

print("Maximum in list:", my_max(*my_list))

print("Maximum in set:", my_max(*my_set))

print("Maximum in tuple:", my_max(*my_tuple))
