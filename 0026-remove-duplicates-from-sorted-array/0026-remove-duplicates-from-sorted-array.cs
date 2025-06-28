public class Solution {
    public int RemoveDuplicates(int[] nums) {
      int write = 1;
      for ( int read = 1; read < nums.Length; read++){
        if(nums[read] != nums[read - 1]){
          nums[write] = nums[read];
          write++;
        } 
      }
      return write;
      

        
    }
}