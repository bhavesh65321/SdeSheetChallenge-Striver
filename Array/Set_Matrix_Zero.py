class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        temp=[]  # store the 0 value matrix index in array then make related row and column zero
        n1=len(matrix)
        n2=len(matrix[0])
        for i in range(n1):
            for j in range(n2):
                if matrix[i][j]==0:
                    temp.append([i,j])
        temp1=len(temp)
        k=0
        while(k<temp1):
            for i in range(n2):
                matrix[temp[k][0]][i]=0
            for i in range(n1):
                matrix[i][temp[k][1]]=0
            k+=1
        return matrix
            
            