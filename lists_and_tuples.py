empty_list = []
print(empty_list)

my_list = [1, 2, 3, 'apple', 3.14]
print(my_list)
print(my_list[0]) # Print first element of the list

sliced_list = my_list[1:4] # Get from 1 to 4 elements from list. The last index is not included.
print(sliced_list)

# Replace element
my_list[3] = 'banana'
print(my_list)

# Length of lists
print(len(my_list))

# Add new element to the list
my_list.append(10)
print(my_list)

# Add new elements from another list
my_list.extend([13, 'banana'])
print(my_list)

# Add new element and it position in the list
my_list.insert(0, 'zero')
print(my_list)

# Count of the same elements in the list
print(my_list.count("banana"))

# Index of the same elements from the list
print(my_list.index("banana"))

