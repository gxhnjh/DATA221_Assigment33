def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain
    keyword (case-insensitive). Line numbers start at 1.
    """
    results = []

    with open(filename, "r", encoding="utf-8") as file:
        for i, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                results.append((i, line.strip()))

    return results


# test the function
matches = find_lines_containing("sample-file (1).txt", "lorem")

# print how many matching lines were found
print("Number of matching lines:", len(matches))

# print the first 3 matching lines
print("First 3 matching lines:")
for line_number, text in matches[:3]:
    print(line_number, text)
