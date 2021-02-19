class Solution:
    def reverse(self, x: int) -> int:
        
        negative = x<0
        num = 0
        if negative:
            x *= -1
        while x != 0 :
            num = num*(10) + (x%10)
            x = x//10
            if num<= -2**31 or num>= 2**31 - 1:
                return 0
        #if num
        return -1 * num if negative else num
