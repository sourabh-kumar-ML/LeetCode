"""TwoSum --> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
           You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
           Solution --> Brute force method. (time-> 49ms, memory->14.5MB)"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) == target:
                    return [i,j]
        # More optimized solution:
        """for idx,num in enumerate(nums):
            val = target - num
            if val in nums[idx+1:]:
                if idx == nums.index(val):
                    return [idx,nums[idx+1:].index(val)+idx+1]
                else : return [idx,nums.index(val)]"""
