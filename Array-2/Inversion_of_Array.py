#1st method TC-o(n**2)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        i=0
        while(i<n):
            temp1=intervals[i]
            j=i+1
            while(j<n):
                temp2=intervals[j]
                if(temp1[1]>=temp2[0]):
                    intervals.pop(j)
                    intervals[i][0]=min(temp1[0],temp2[0])
                    intervals[i][1]=max(temp1[1],temp2[1])
                    n=n-1
                else:
                    j+=1
            i+=1
        return intervals



#2nd method with TC of o(nlogn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        i=0
        while(i<n-1):
            temp1=intervals[i]
            if(temp1[1]>=intervals[i+1][0]):
                temp2=intervals[i+1]
                intervals.pop(i+1)
                intervals[i][0]=min(temp1[0],temp2[0])
                intervals[i][1]=max(temp1[1],temp2[1])
                n=n-1
            else:
                i+=1
        return intervals
            