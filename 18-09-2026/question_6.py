# 6. Count Character Frequency in a String
text = "python programming"
freq = {}
for char in text:
    if char != " ":
        freq[char] = freq.get(char, 0) + 1
print("String:", text)
print("Character frequency:", freq)
