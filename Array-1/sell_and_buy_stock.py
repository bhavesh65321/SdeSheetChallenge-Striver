from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max1=0
        temp1=prices[0]
        for i in prices:
            if(i>=temp1):
                if((i-temp1)>max1):
                    max1=i-temp1
            else:
                temp1=i
        return max1
        