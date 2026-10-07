def first_non_repeating(s):
    freq = {}


    for char in s:
        freq[char] = freq.get(char, 0) + 1


    for char in s:
        if freq[char] == 1:
            return char
    return None

print(first_non_repeating("swiss")) # w
print(first_non_repeating("aabbcc")) # None
print(first_non_repeating("programming")) # p