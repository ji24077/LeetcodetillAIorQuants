public class Solution {
    public int LargestAltitude(int[] gain) {
      int maxAltitudes = 0;
      int current = 0; //our prefixsum.

      foreach(int g in gain){
        current += g;
        maxAltitudes = Math.Max(current, maxAltitudes);

      }
      return maxAltitudes;
        
    }
}