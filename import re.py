import re

# List of words
word_list = ["pastel de belem", "another_word", "yet_another_word"]

# The string to match
pattern = "PAS.E.....B...M"

# Replace 'x' with '.' to match any character, and ' ' with '\s*' to match any number of spaces
# Compile the pattern
compiled_pattern = re.compile(pattern, re.I)

# Iterate through the word list and check for matches
matching_words = [word for word in word_list if compiled_pattern.search(word)]

# Print the matching words
print(matching_words)
