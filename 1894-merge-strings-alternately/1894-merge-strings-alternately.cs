public class Solution {
    public string MergeAlternately(string word1, string word2) {
      int left = 0;
      int right = 0;
      StringBuilder solution = new StringBuilder(); //like an array for string
      //since String[] is immutable.
      while(left < word1.Length || right < word2.Length){
        if(left < word1.Length){
          solution.Append(word1[left++]);
        }
        if(right< word2.Length){
          solution.Append(word2[right++]);
        }
      }
      return solution.ToString();
    }
}