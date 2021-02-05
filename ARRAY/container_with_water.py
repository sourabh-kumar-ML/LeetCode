class Solution:
    def maxArea(self, height: List[int]) -> int:
        #Best Method all test case pases
        """mx_area,l,r = 0,0,len(height)-1
        while(l<r):
            mx_area = max(mx_area,min(height[l],height[r])*(r-l))
            if (height[l]<height[r]):
                l+=1
            else:
                r-=1
        return mx_area"""
        
        #Brute force approach time limit exceeds
        """area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = max(area,min(height[i],height[j])*(j-i))
        return area"""
