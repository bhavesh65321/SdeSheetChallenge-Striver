
#to find the next permutation first we find num1 element those break the order of increasing order from end and then one more time we find element that is less then num1,then we swap both element and from next to num1 we sort in decresing order bcoz we made left part highest so,right part is lowest that is the next greater permutation or subset.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        a=nums
        temp1=0
        if(n==1):
            return a
        for i in range(n-2,-1,-1):
            if(a[i]<a[i+1]):
                temp1=i
                break
        temp2=n-1
        for i in range(n-1,-1,-1):
            if(a[temp1]<a[i]):
                temp2=i
                break

        a[temp1],a[temp2]=a[temp2],a[temp1]
        tempx=[]
        for i in range(temp1+1,n):
            tempx.append(a[i])
        tempx.sort()
        j=temp1+1
        for i in range(len(tempx)):
            a[j]=tempx[i]
            j+=1
        
        
        
        return a
        
        """
        Do not return anything, modify nums in-place instead.
        """
    