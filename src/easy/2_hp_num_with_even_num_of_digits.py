class Solution:
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            if len(str(i))%2 == 0:
                count += 1
        return count

# Step 1: Iterating through each element in the list
# Step 2: Converting each element from integer to string (so that we can find the length)
# Step 3: Check if the length of the element is divisible by 2
# Step 4: Counting the number of length of the elements /2 and returning the count value.