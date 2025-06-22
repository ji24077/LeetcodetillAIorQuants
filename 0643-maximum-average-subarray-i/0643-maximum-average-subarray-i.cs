public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
      double WindowSum = 0 ;
      int n = nums.Length;
      for(int i = 0; i < k; i++){
        WindowSum += nums[i];
      }
      double avg = WindowSum/k;
      //now we have todo sliding window: take out first, add next.
      for(int i = k; i < n; i++){
        WindowSum += nums[i] - nums[i - k];
        avg = Math.Max(avg, WindowSum/k);

      }
      return avg;

    }
}