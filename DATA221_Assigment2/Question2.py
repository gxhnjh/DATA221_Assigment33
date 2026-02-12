# Open and read the file
file_path = r"C:\Users\omers\Downloads\sample-file (1).txt"

file = open(file_path, "r")
text = file.read()
file.close()

# Split into words
tokens = text.split()

clean_tokens = []

# Punctuation we want to remove
punctuation = ".,!?;:'\"()[]{}<>-"

# Clean the tokens
for word in tokens:
    # Make lowercase
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

# Build bigrams (pairs of consecutive words)
bigrams = []

for i in range(len(clean_tokens) - 1):
    pair = clean_tokens[i] + " " + clean_tokens[i + 1]
    bigrams.append(pair)

# Count bigram frequencies
bigram_counts = {}

for bg in bigrams:
    if bg in bigram_counts:
        bigram_counts[bg] += 1
    else:
        bigram_counts[bg] = 1

# Sort by frequency (descending)
sorted_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)

# Print top 5
for bg, count in sorted_bigrams[:5]:
    print(bg, "->", count)
