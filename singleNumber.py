"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

def singleNumber(self, nums: List[int]) -> int:

    ## Initialize Dictionary
    num_count = {}

    # Count the occurences of each number in the array
    for num in nums:
        if num in num_count:
            num_count[num] +=1
        else:
            num_count[num] = 1

    # Find the number with count 1
    for num, count in num_count.items():
        if count == 1:
            return num
