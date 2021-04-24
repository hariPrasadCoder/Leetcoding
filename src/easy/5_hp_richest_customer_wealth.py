class Solution:
    def maximumWealth(self, accounts) -> int:
        final = []
        for customer_accounts in accounts:
            wealth = 0
            for per_bank in customer_accounts:
                wealth += per_bank
            final.append(wealth)
        return (max(final))

# Step 1: Iterate through each customers and add their total value in every banks
# Step 2: Store those values in a list and return the maximum value of the list