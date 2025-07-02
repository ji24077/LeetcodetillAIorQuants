public class Solution {
    public int LengthOfLongestSubstring(string s) {
      //HashSet<char> charSet = new.. // store set of char of curr window.
      //int left = 0 , int right=0, 
      //fixed the left, and move right untill same letter as left comesout.
      //if it overlaps with left, u move left pointer.
      HashSet<char> charSet = new HashSet<char>();
      int left = 0;
      int result = 0;
      for(int right = 0; right < s.Length; right++){
        while(charSet.Contains(s[right])){
          //its overlaps.
          charSet.Remove(s[left]);
          left++;

        }
        charSet.Add(s[right]);
        result = Math.Max(result, right - left + 1); // update to max.
      }   
      return result;   



        
    }
}