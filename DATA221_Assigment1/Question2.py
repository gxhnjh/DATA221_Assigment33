# This function builds a nested dictionary from a list of strings
# Each string becomes a key and the value stores the length and if its even or odd
def build_nested_dictionary_from_string_list(list_of_strings):

    # Creating an empty dictionary to store the final results
    nested_dictionary_result = {}

    # Loop through each string in the list
    for current_string in list_of_strings:

        # Find the length of the current string
        length_of_current_string = len(current_string)

        # Check if the length is even or odd
        if length_of_current_string % 2 == 0:
            parity_of_string_length = "even"
        else:
            parity_of_string_length = "odd"

        # Store the results in the dictionary using the string as the key
        nested_dictionary_result[current_string] = {
            "length": length_of_current_string,
            "parity": parity_of_string_length
        }

    # Return the completed nested dictionary
    return nested_dictionary_result


# Ask the user to enter words separated by commas
user_input_string = input("Enter a list of words separated by commas: ")

# Split the input string into a list using commas as separators
list_of_user_strings = user_input_string.split(",")

# Create an empty list to store cleaned words
cleaned_list_of_user_strings = []

# Remove extra spaces from each word and add it to the cleaned list
for word in list_of_user_strings:
    cleaned_list_of_user_strings.append(word.strip())

# Build the nested dictionary using the cleaned list of words
final_nested_dictionary = build_nested_dictionary_from_string_list(cleaned_list_of_user_strings)

# Print the final result
print("\nFinal Nested Dictionary:")
print(final_nested_dictionary)