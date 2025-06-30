public class Solution {
    public int RemoveDuplicates(int[] nums) 
    {
      //just count original when search pointer's value is not eqaul to original's
        int original = 0;

        for(int search = 0; search < nums.Length; search++){
          if(original < 2 || nums[search] != nums[original -2]){
            nums[original] = nums[search];
            original++;

          }

        }
        return  original;

    }
}