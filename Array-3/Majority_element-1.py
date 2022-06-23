#1st approach using O(nlogn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        temp=1
        ans=1
        temp2=nums[0]
        temp1=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==temp1:
                temp+=1
            else:
                temp=1
                temp1=nums[i]
            if(temp>ans):
                ans=temp
                temp2=nums[i]
        return temp2