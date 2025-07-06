'''
| Type        | Description                 | When to Use                           |
| ----------- | --------------------------- | ------------------------------------- |
| Memoization | Top-down, recursion + cache | Easy to write, good for trees/graphs  |
| Tabulation  | Bottom-up, iteration        | More efficient, no recursion overhead |


'''

class Solution:
    def rec(self,n,dp):
        if n==1 or n==0:
            return n
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.rec(n-1,dp)+self.rec(n-2,dp)
        return dp[n]
    

    def fibo(self,n):
        dp=[-1]*(n+1)

        return self.rec(n,dp)
    



sol=Solution()
x=sol.fibo(5)
print(x)




