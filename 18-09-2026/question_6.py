# 6. Count character frequency in a string.
text = "python"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("Character frequency:", freq)
