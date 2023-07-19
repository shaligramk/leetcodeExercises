"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
"""

def containsDuplicate(self, nums: List[int]) -> bool:

	numSet = set()

	for num in nums:
		if num in numSet:
			return True
		else:
			numSet.add(num)

	return False
