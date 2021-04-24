class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        final = 0
        for j in nums:
            final = final ^ j
        return final

# Step 1: Populating the list 'nums' using the given condition (start + 2*i)
# Step 2: Performing XOR operation in the 'nums' list and returning the output
