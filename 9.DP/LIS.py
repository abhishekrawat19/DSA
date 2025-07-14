class Solution:
    def rec(self, i, prev, nums):
        if i == len(nums):
            return 0

        take = 0
        if prev == -1 or nums[prev] < nums[i]:
            take = 1 + self.rec(i + 1, i, nums)

        not_take = self.rec(i + 1, prev, nums)

        return max(take, not_take)

    def lengthOfLIS(self, nums):
        return self.rec(0, -1, nums)




sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Output: 4



class Solution2:
    def rec(self, i, prev_index, nums, dp):
        if i == len(nums):
            return 0

        if dp[i][prev_index + 1] != -1:
            return dp[i][prev_index + 1]

        take = 0
        if prev_index == -1 or nums[prev_index] < nums[i]:
            take = 1 + self.rec(i + 1, i, nums, dp)

        not_take = self.rec(i + 1, prev_index, nums, dp)

        dp[i][prev_index + 1] = max(take, not_take)
        return dp[i][prev_index + 1]

    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.rec(0, -1, nums, dp)
    

class Solution3:
    def lowerbound(self, arr, target):
        low, high = 0, len(arr) - 1
        ans = len(arr)  # Default: insert at end if target is greater than all
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans

    def lengthOfLIS(self, nums):
        lis = []
        n = len(nums)
        lis.append(nums[0])

        for i in range(1, n):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                lb = self.lowerbound(lis, nums[i])
                lis[lb] = nums[i]

        return len(lis)
