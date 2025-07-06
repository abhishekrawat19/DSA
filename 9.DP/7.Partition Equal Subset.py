class Solution:
    def rec(self, i, sum1, nums, total):
        if sum1 > total:
            return False
        elif sum1 == total:
            return True
        elif i == len(nums):
            return False
        
        # Try taking the current element
        take = self.rec(i + 1, sum1 + nums[i], nums, total)
        
        # Try skipping the current element
        not_take = self.rec(i + 1, sum1, nums, total)

        return take or not_take  

    def canPartition(self, nums):
        n = len(nums)
        if n == 1:
            return False
        total = sum(nums)
        if total % 2 == 1:
            return False

        return self.rec(0, 0, nums, total // 2)  # total//2 is the correct target
