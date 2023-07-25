"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
def isPalindrome(self, s: str) -> bool:

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Compare characters from both ends of the string
    left = 0
    right = len(cleaned_string) - 1
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
        
    return True

# Test cases
print(is_valid_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_valid_palindrome("race a car"))  # False
print(is_valid_palindrome("level"))  # True
print(is_valid_palindrome("No 'x' in Nixon"))  # True