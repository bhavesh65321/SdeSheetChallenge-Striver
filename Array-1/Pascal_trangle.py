class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        ans=[[1]]  #print Pascal Trangle like 1
                   #                         1  1
                   #                        1  2  1
                   #                       1  3  3  1
        if n==1:
            return ans
        elif n==2:
            ans=[[1],[1,1]]
        else:
            ans=[[1],[1,1]]
            n=n-2
            t=1
            while(n>0):
                temp=[]
                temp.append(1)
                temp2=ans[t]
                for i in range(len(ans[t])-1):
                    temp.append(temp2[i]+temp2[i+1])
                temp.append(1)
                ans.append(temp)
                t+=1
                n-=1
        return ans