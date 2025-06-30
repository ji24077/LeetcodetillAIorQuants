public class Solution {
    public int ClimbStairs(int n) {
      // if( n == 0 || n == 1){
      //   return 1;
      // }
      // return ClimbStairs(n -1) + ClimbStairs(n -2);

      int dp0 = 1;
      int dp1 = 1;

      for(int i = 2; i <= n; i++) {
        int dpi = dp0 + dp1;
        dp0 = dp1;
        dp1 = dpi;

      }
      return dp1;
        

    }
}