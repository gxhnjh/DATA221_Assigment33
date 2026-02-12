# Open and read the file
file_path = "C:\\Users\\omers\\Downloads\\sample-file (1).txt"


file = open(file_path, "r")
text = file.read()
file.close()

# Split into words
tokens = text.split()

clean_tokens = []

# Punctuation we want to remove
punctuation = ".,!?;:'\"()[]{}<>-"

for word in tokens:
    # Make them lowercase
    word = word.lower()

    # Remove punctuation from start and end
    word = word.strip(punctuation)

    # Count alphabet letters
    alpha_count = 0
    for ch in word:
        if ch.isalpha():
            alpha_count += 1

    # Keep words with at least 2 letters
    if alpha_count >= 2:
        clean_tokens.append(word)

# Count frequencies using a dictionary
word_counts = {}

for w in clean_tokens:
    if w in word_counts:
        word_counts[w] += 1
    else:
        word_counts[w] = 1

# Sort by count
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print top 10
for word, count in sorted_words[:10]:
    print(word, "->", count)
