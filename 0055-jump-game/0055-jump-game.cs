public class Solution {
    public bool CanJump(int[] nums) {
      int maxReach = 0;
      //maxReach = i + nums[i],
      for(int i = 0; i < nums.Length; i++){
        
        
        if(maxReach >= nums.Length - 1){ // reach the end.
          return true;
        }
        // else return false를 하면바로return 해서 안됨.
        else if(i > maxReach){
          return false;
        }
        maxReach = Math.Max(maxReach, i + nums[i]);
       
      }
      return true;

        
    }
}