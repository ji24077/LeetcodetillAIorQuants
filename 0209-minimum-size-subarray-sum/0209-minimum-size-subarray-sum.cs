public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
      // left = 0;
      //int sum = 0;
      //right for in range(nums)
      //sum+= nums[right]
      //while( sum >= target) // update min len, sum, move left pointer,

      //return if minLength inf, return 0 ow return minlen.


      int n = nums.Length;
      int left = 0;
      int sum = 0;
      int minLen = int.MaxValue; // minLen = inf.
       

      for (int right = 0; right < n; right++){
        sum += nums[right]; //sliding window.
        while(sum >= target){
          int currLen = right - left + 1;
          minLen = Math.Min(minLen, currLen); // currL = right - left + 1
          sum -= nums[left];
          left++;

        }
      }
      //we found the minLen of target that consecutively satsifies.

      return (minLen == int.MaxValue) ? 0 : minLen;



        
    }
}