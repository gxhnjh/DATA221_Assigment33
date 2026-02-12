from random import random

# Generate a list of random values between 0 and 1
list_of_random_values = [random() for i in range(20)]

# Generate a random comparison value x
comparison_value_x = random()
# Sort the list
sorted_list_of_values = sorted(list_of_random_values)


# Find all indices where value >= x
list_of_matching_indices = []

for index_position in range(len(sorted_list_of_values)):
    if sorted_list_of_values[index_position] >= comparison_value_x:
        list_of_matching_indices.append(index_position)


# Print results
print("Sorted list:")
print(sorted_list_of_values)

print("\nComparison value x:")
print(comparison_value_x)

if len(list_of_matching_indices) > 0:
    print("\nFirst matching index:")
    print(list_of_matching_indices[0])
else:
    print("\nNo values were greater than or equal to x")