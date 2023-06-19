"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        input - > list of integars
        input --> target - > sum of integars
        output-> pair of ints [list]
        """
        if not nums:
            return 0
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                k = nums[i] + nums[j]
                if k == target:
                    return [i,j]
