public class Solution {
    public IList<string> SummaryRanges(int[] nums) {


      List<string> result = new List<string>();

      int n = nums.Length;
      if( n == 0 ){
        return result;
      }
      int start = nums[0];

      //nums[i] - nums[i- 1] = 1
      for ( int i = 1; i <= n; i++){
        if(i == n || nums[i] != nums[i -1] +1)
        {
          if ( start == nums[ i - 1]){
            result.Add(start.ToString());
            //7
          }
          else{
            result.Add(start + "->" + nums[i-1]);
             // 0 -> 2
          }
          if ( i < n){
            start = nums[i];
          }


        }
      }
      return result;
        
    }
}