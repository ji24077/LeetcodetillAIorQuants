public class Solution {
    public int PivotIndex(int[] nums) {
        int leftSum = 0;
        int total = 0;
        int n = nums.Length;
        for(int i = 0; i < n; i++){
          total += nums[i];
        }
        //now total is made it.
        for(int i = 0; i < n; i++){
          int rightSum = total - leftSum - nums[i];
          if(rightSum == leftSum){
            return i;
          }
          //ow update the leftSum:
          leftSum += nums[i];


        }
        return -1;
    }
}