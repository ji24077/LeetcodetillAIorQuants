public class Solution {
    public int LengthOfLastWord(string s) {
      //start form end index.
      //u skip when ever its space
      //int count, count++ if it sees the characters
      //if space -> stop.

      int count = 0;
      int i = s.Length - 1;
      while ( i >=0 && s[i] == ' '){
        i--;
      }
      while(i>=0 && s[i] != ' '){
        count++;
        i--;
      }
      return count;
        
    }
}