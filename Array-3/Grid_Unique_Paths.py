#1st approach using recursion TC-o(2**(m+n)) sc-O(1)
class Solution:
    def count(self,i,j,m,n):
        if(i==(m-1) and j==(n-1)):
            return 1
        elif(i>=m or j>=n):
            return 0
        else:
            return self.count(i+1,j,m,n)+self.count(i,j+1,m,n)
        
    def uniquePaths(self, m: int, n: int) -> int:
        i=0
        j=0
        return self.count(i,j,m,n) 



#2nd approach using DP TC-O(m*n) SC-O(m*n)


class Solution:
    def count(self,i,j,m,n,dp):
        if(i==(m-1) and j==(n-1)):
            return 1
        elif(i>=m or j>=n):
            return 0
        else:
            if(dp[i][j]!=-1):
                return dp[i][j]
            else:
                return self.count(i+1,j,m,n,dp)+self.count(i,j+1,m,n,dp)
        
    def uniquePaths(self, m: int, n: int) -> int:
        i=0
        j=0
        dp=[[-1 for i in range(n)]for j in range(m)]
        return self.count(i,j,m,n,dp)  


#3rd and efficient approach using all possible combination

 def uniquePaths(self, m: int, n: int) -> int:
        temp1=(m+n-2)
        temp2=(m-1)
        ans1=1
        for i in range(temp2):
            ans1=ans1*temp1
            temp1-=1
        ans2=1
        for i in range(temp2,0,-1):
            ans2=ans2*i
        return int(ans1/ans2)
        
        