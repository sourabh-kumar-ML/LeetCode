class Solution:
    def convert(self, s: str, numRows: int) -> str:
        hashmap = {}
        num = 0
        val = 1
        
        if numRows == 1:
            return s
        
        for i in range(numRows):
            hashmap[i] = ''
        
        for i in range(len(s)):
            hashmap[num]+=(s[i])
            num += val
            if num == 0 or num == numRows-1 :
                val *= -1
                
        string = ''
        for val in hashmap.values():
            string+= val
        
        return string
