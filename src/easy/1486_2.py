class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1,n):
            res^=start+2*i
        return res


## Intuition:
# As per the requirements of the problem, we don't need to return the array itself.
# So, we can free up any space that would have been otherwise allocated to the array 
# And instead work with the elements of the array generated each iteration 
# without storing them in a temporary location     