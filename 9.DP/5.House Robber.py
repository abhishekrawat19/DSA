# House Robber Problem 

class Solution:
    def rec(self,i,nums):
        if i >= len(nums):
            return 0
        # take case
        take=nums[i]+self.rec(i+2,nums)

        # not take
        not_take=self.rec(i+1,nums)
        return max(take,not_take)


    def rob(self,nums):
        return self.rec(0,nums)
    



class Solution1:
    def rec(self, i, nums, dp):
        if i >= len(nums):
            return 0

        if dp[i] != -1:
            return dp[i]

        # take this house
        take = nums[i] + self.rec(i + 2, nums, dp)

        # skip this house
        not_take = self.rec(i + 1, nums, dp)

        dp[i] = max(take, not_take)
        return dp[i]

    def rob(self, nums):
        n = len(nums)
        dp = [-1] * n  # -1 means "not computed yet"
        return self.rec(0, nums, dp)

