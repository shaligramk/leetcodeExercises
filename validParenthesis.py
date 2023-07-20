"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(self, string: str) -> bool:

	# Initialize an empty stack to keep track of opening brackets.
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'} 
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    # Iterate through each character in the input string.
    for char in string:
        if char in opening_brackets:  # If the character is an opening bracket.
            stack.append(char)  # Push it onto the stack.
        elif char in closing_brackets:  # If the character is a closing bracket.
            if len(stack) == 0:  # If the stack is empty, there is no matching opening bracket for this closing bracket.
                return False
            top = stack.pop()  # Pop the top element from the stack (last added opening bracket).
            if bracket_pairs[top] != char:  # Check if the closing bracket matches the last opening bracket.
                return False

    # After processing all characters, if there are remaining brackets in the stack, it means they are unclosed.
    return len(stack) == 0  # If the stack is empty, all brackets were properly closed and balanced.
