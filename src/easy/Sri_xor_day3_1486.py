# Credits: https://github.com/sriinampudi

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums =[]
        c = start
        for i in range (0,n):
            nums.append(start+(2*i))
            if(i>0):
                c = c ^ nums[i]
                
        return(c)
            
            
            