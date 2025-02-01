# 1. Sum all items in a list

def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

list = [1, 1, 2, 3, 4, 4, 5, 1]
print("Sum of list items:", sum_list(list))
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Find largest and smallest number without builtin functions

def find_min_max(lst):
    smallest = lst[0]
    largest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

smallest, largest = find_min_max(lst)
print("Smallest:", smallest, "Largest:", largest)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Find duplicate values in a list

def find_duplicates(lst):
    duplicates = []
    seen = {}
    for num in lst:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for key, value in seen.items():
        if value > 1:
            duplicates.append(key)
    return duplicates

print("Duplicate values:", find_duplicates(lst))
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Split a list into two parts with a given length for the first part

def split_list(lst, first_part_length):
    return lst[:first_part_length], lst[first_part_length:]

first_part_length = 3
part1, part2 = split_list(lst, first_part_length)
print("Splitted the said list into two parts:", (part1, part2))
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5. Traverse list in reverse order and print elements with original index

def traverse_reverse(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(lst[i])

color_list = ['red', 'green', 'white', 'black']
print("Traverse the said list in reverse order:")
traverse_reverse(color_list)
'''
