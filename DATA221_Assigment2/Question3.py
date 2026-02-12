import string

# File path
file_path = r"C:\Users\omers\Downloads\sample-file (1).txt"


# Function to normalize a line
def normalize_line(line):
    # Convert to lowercase
    line = line.lower()

    # Remove whitespace
    line = line.replace(" ", "")

    # Remove punctuation
    for char in string.punctuation:
        line = line.replace(char, "")

    return line


# Read the file
file = open(file_path, "r")
lines = file.readlines()
file.close()

# Dictionary to store normalized lines
duplicate_sets = {}

# Loop through each line
for i in range(len(lines)):
    original_line = lines[i].strip()

    if original_line == "":
        continue  # Skip empty lines

    normalized = normalize_line(original_line)

    if normalized not in duplicate_sets:
        duplicate_sets[normalized] = []

    duplicate_sets[normalized].append((i + 1, original_line))

# Find only sets with duplicates
near_duplicate_groups = []

for key in duplicate_sets:
    if len(duplicate_sets[key]) > 1:
        near_duplicate_groups.append(duplicate_sets[key])

# Print number of sets
print("Number of near-duplicate sets:", len(near_duplicate_groups))

# Print first two sets
print("\nFirst two sets found:")
for group in near_duplicate_groups[:2]:
    print("\nSet:")
    for line_num, text in group:
        print(line_num, ":", text)
