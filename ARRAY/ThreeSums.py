class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i,num in enumerate (nums):
            l,r=i+1,len(nums)-1
            if i>0 and nums[i-1] == num:
                continue
            while l<r :
                value = num+ nums[l] + nums[r]
                if value < 0:
                    l+=1
                elif value >0:
                    r-=1
                else:
                    result.append([num,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        
        return result
