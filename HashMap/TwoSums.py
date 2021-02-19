class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,num in enumerate(nums):
            val = target-num
            if val in hashmap:
                return [hashmap[val],i]
            else : hashmap[num] = i
