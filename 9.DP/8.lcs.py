
class Solution:
    def rec(self,i,j,text1,text2):
        if i>=len(text1) or j>=len(text2):
            return 0
        
        ans=0
        if text1[i]==text2[j]:
            ans=1+self.rec(i+1,j+1,text1,text2)

        else:
            ans =max(self.rec(i,j+1,text1,text2),self.rec(i+1,j,text1,text2))

            return ans

    
    def lcs(self,text1,text2):

        return self.rec(0,0,text1,text2)
    



class Solution1:
    def rec(self,i,j,text1,text2,dp):
        if i>=len(text1) or j>=len(text2):
            return 0
        
        ans=0

        if dp[i][j]!=-1:
            return dp[i][j]
        if text1[i]==text2[j]:
            ans=1+self.rec(i+1,j+1,text1,text2)

        else:
            ans =max(self.rec(i,j+1,text1,text2),self.rec(i+1,j,text1,text2))

        dp[i][j]=ans
        return dp[i][j]

    
    def lcs(self,text1,text2):
       dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
       return self.rec(0,0,text1,text2,dp)
    




class Solution3:    
    def lcs(self, text1, text2):
        n=len(text1) 
        m= len(text2)
        
        # Initialize dp table with size (m+1) x (n+1) and all values 0
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # Fill dp table
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

    


