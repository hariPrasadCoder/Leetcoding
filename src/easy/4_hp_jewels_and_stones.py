class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_list = list(jewels)
        count = 0
        for stone in stones:
            if stone in jewel_list:
                count += 1
        return count

# Step 1: Converting string 'jewels' into a list
# Step 2: Iterate through each stone and check whether it's in the jewel list or not