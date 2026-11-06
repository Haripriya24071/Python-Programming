# 6. Given a list of words, extract words ending with the letter 'n' and calculate their lengths.

a = ["pen", "apple", "fan", "book", "train"]

b = list(filter(lambda x: x.endswith('n'), a))
c = list(map(lambda x: len(x), b))

print("Words ending with n:", b)
print("Lengths:", c)

