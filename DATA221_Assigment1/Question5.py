import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    """
    Calculates the percentage of the larger circle's area
    that can be covered by the smaller circle.

    Both radii must be positive integers.
    """

    # Check that both inputs are integers
    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Both radii must be positive integers."

    # Check that both inputs are positive
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Both radii must be positive integers."

    # Calculate the area of the first circle
    areaOfCircle1 = math.pi * (radiusOfCircle1 ** 2)

    # Calculate the area of the second circle
    areaOfCircle2 = math.pi * (radiusOfCircle2 ** 2)

    # Determine which area is larger and smaller
    if areaOfCircle1 > areaOfCircle2:
        largerArea = areaOfCircle1
        smallerArea = areaOfCircle2
    else:
        largerArea = areaOfCircle2
        smallerArea = areaOfCircle1

    # Calculate percentage coverage
    percentageCoverage = (smallerArea / largerArea) * 100

    return percentageCoverage


# -------------------------
# Main Program
# -------------------------

# Ask the user for input
userRadius1 = input("Enter the radius of the first circle: ")
userRadius2 = input("Enter the radius of the second circle: ")

# Check that inputs are numbers before converting
if not userRadius1.isdigit() or not userRadius2.isdigit():
    print("Both radii must be positive integers.")
else:
    # Convert inputs to integers
    radiusOfCircle1 = int(userRadius1)
    radiusOfCircle2 = int(userRadius2)

    # Call the function and print result
    result = circleAreaCoverage(radiusOfCircle1, radiusOfCircle2)
    print("Percentage of coverage:", result, "%")
