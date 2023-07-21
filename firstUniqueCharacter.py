"""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
"""

def first_unique_char(s):
    # Dictionary to store character frequencies
    char_count = {}
    index = 0

    # Count the occurrences of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character in the original order
    for char in s:
        if char_count[char] == 1:
            return index
        index += 1

    # If no non-repeating character is found, return -1
    return -1
