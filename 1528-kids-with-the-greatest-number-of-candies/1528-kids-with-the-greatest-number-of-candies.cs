public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
      List<bool> result = new List<bool>();
      int max = 0;
      foreach( int c in candies){
        if(c >= max){
          max = c; // update the max.
        }
      }
      //after updated the max.
      foreach(int c in candies){
            result.Add(c + extraCandies >= max);

      }
      return result;
        
    }
}