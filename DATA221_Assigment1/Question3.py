#Function that computes x to the y
def compute_power_of_two_numbers(base_number, exponent_number):
    return base_number ** exponent_number


#Example input list
list_of_number_pairs = [[2, 3], [1, -1], [6, 5], [3, 0]]

# List to store valid results
list_of_valid_results = []

# Loop through each pair using argument unpacking
for base_value, exponent_value in list_of_number_pairs:

    # Skip if the exponent is negative
    if exponent_value < 0:
        continue

    # Compute the power and store the result
    power_result = compute_power_of_two_numbers(base_value, exponent_value)
    list_of_valid_results.append(power_result)

# Print the final list of results
print("Final list of valid results:")
print(list_of_valid_results)