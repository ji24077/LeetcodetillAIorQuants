public class Solution {
    public void MoveZeroes(int[] nums) {
      int InsertZeroPlace = 0;
      for(int i = 0; i < nums.Length; i++){
        if(nums[i] != 0){
          nums[InsertZeroPlace] = nums[i];
          InsertZeroPlace++;
        }
      }
      //there is place that zero has to be placed.
      while(InsertZeroPlace < nums.Length){
        nums[InsertZeroPlace] = 0;
        InsertZeroPlace++;
      }
    }
}