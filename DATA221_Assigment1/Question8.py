import pandas as pd

# Given data
data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create the DataFrame
dataFrame = pd.DataFrame(data)

# Add a new computed column
# This example multiplies column A and B, then adds column C
dataFrame["Computed"] = (dataFrame["A"] * dataFrame["B"]) + dataFrame["C"]

# Print the final DataFrame
print(dataFrame)
