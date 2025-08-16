class Solution:
    def nextGreaterElement(self, nums1, arr):
        stack = []
        ans = {}  # To store next greater element for each number in arr (nums2)
        n = len(arr)

        # Traverse arr (nums2) from right to left
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()

            # Assign next greater element
            if len(stack) == 0:
                ans[arr[i]] = -1
            else:
                ans[arr[i]] = stack[-1]

            # Push current element onto stack
            stack.append(arr[i])

        # Build result for nums1 using the map
        result = []
        for i in nums1:
            result.append(ans[i])

        return result

# --------- Test the function ---------
if __name__ == "__main__":
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    sol = Solution()
    res = sol.nextGreaterElement(nums1, nums2)
    print("Next greater elements:", res)
