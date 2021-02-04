class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for j in nums2:
            nums1.append(j)
        nums1.sort()
        total_len = len(nums1)

        if total_len%2 ==0:
            x=total_len//2-1
            y=x+1
           
            return (nums1[x]+nums1[y])/2
        else:
            return (nums1[total_len//2])
