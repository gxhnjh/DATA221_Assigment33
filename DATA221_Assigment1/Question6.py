def distributionAnalysis(numbersList):
    """
    Receives a list of numbers and returns a dictionary where:
    - Each key is a unique value from the list
    - Each value is the percentage of elements in the list
      that are less than or equal to that key
    The dictionary is sorted by key before being returned
    """

    # Check that the list is not empty
    if len(numbersList) == 0:
        return "The list cannot be empty."

    # Check that all values in the list are numbers (int or float)
    for value in numbersList:
        if not isinstance(value, (int, float)):
            return "All values in the list must be numbers."

    totalElements = len(numbersList)

    # Create a list of unique values and sort it
    uniqueValues = sorted(set(numbersList))

    # Create an empty dictionary to store results
    distributionDictionary = {}

    # Loop through each unique value
    for key in uniqueValues:
        countLessOrEqual = 0

        # Count how many values are less than or equal to the key
        for number in numbersList:
            if number <= key:
                countLessOrEqual += 1

        # Calculate percentage
        percentage = (countLessOrEqual / totalElements) * 100

        # Store in dictionary
        distributionDictionary[key] = percentage

    return distributionDictionary


# -------------------------
# Main Program
# -------------------------

# Ask user to enter numbers separated by spaces
userInput = input("Enter a list of numbers separated by spaces: ")

# Split input into a list of strings
inputList = userInput.split()

numbersList = []

# Convert input values to numbers
for value in inputList:
    try:
        numbersList.append(float(value))
    except:
        print("All values must be numbers.")
        numbersList = []
        break

# Run function if input is valid
if len(numbersList) > 0:
    result = distributionAnalysis(numbersList)
    print("Distribution Dictionary:")
    print(result)
