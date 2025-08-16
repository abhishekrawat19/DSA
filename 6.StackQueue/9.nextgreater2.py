class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums+=nums
        n=len(nums)
        st=[]
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while st and st[-1]<=nums[i]:
                st.pop()

            if len(st)==0:
                ans[i]=-1
            else:
                ans[i]=st[-1]

            st.append(nums[i])


        return ans[:len(ans)//2]
                
        