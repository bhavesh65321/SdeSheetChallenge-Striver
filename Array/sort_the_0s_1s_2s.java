//count no of 0s and 1s then 
//set 0s and 1s in array 


class Solution
{
    public void sortColors(int[] nums) 
    {
        int t1=0;
        int t2=0;
        int n=nums.length;
        for(int i=0;i<n;i++)
        {
            if(nums[i]==0)
            {
                t1+=1;
            }
            if(nums[i]==1)
            {
                t2+=1;
            }
        }
        for(int i=0;i<n;i++)
        {
            if(i<t1)
            {
                nums[i]=0;
            }
            else if(i>=t1 && i<(t1+t2))
            {
                nums[i]=1;
            }
            else
            {
                nums[i]=2;
            }
            
        }
    }
}