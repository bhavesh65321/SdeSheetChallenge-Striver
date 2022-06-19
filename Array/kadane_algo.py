#1st method using 2 for loop and find all possible subarray sum out of them return maximun sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=sum(nums)
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                if(s>temp):
                    temp=s
        return temp


#2nd method using kadane algo that's make more efficient approach we start travesing array from start and add value in variable if at any position we get negative value then we make it zero and igonre all previous element. if we find sum greater then normal sum we replace with max 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msf=nums[0]
        meh=0
        n=len(nums)
        for i in range(n):
            meh+=nums[i]
            if(meh>msf):
                msf=meh
            if(meh<0):
                meh=0
        return msf
                