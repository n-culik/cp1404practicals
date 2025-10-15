"""
CP1404 Practical
Word occurrences count
Date: 15.10.2025
Author: Nicola Culik
Estimate: 40 min
Actual:
"""
word_to_count = {}

text = input("Text: ")
words = sorted(text.split())
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

word_length = max(len(word) for word in words)

for word, count in word_to_count.items():
    print(f"{word:{word_length}} : {count}")