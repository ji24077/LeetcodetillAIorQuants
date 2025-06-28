public class Solution {
    public int RemoveElement(int[] nums, int val) {
      int write = 0;
      int n = nums.Length;
      int count = 0;
      for(int read = 0; read < n; read++){
        if(nums[read] != val){
          nums[write] = nums[read];
          write++;
          
        }

      }
      return write;
     
        
    }
}