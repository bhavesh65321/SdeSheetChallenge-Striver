#using o(n) TC

from ast import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp=0
        i=0
        n=len(matrix)
        m=len(matrix[0])
        while(i<n):
            if(matrix[i][m-1]>target):
                temp=i
                break
            elif(matrix[i][m-1]==target):
                return True
            else:
                i+=1
        temp2=matrix[temp]
        l=0
        r=m-1
        while(l<=r):
            mid=(l+r)//2
            if temp2[mid]==target:
                return True
            elif(temp2[mid]<target):
                l=mid+1
            else:
                r=mid-1
        return False