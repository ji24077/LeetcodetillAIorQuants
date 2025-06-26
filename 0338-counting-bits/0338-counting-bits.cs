public class Solution {
    public int[] CountBits(int n) {
      int[] dp = new int[n+1];
      dp[0] = 0; // 0-->0
      
      for(int i = 0; i <=n; i++){
        dp[i] = dp[i / 2] + (i % 2); // 수학적으로 완전히 동일
      }
      return dp;

        
    }
}