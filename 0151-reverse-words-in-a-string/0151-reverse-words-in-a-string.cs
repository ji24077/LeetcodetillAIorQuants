public class Solution {
    public string ReverseWords(string s) {
      Console.WriteLine(s);
      s = s.Trim();


      List<string> words = new List<string>();
      int i = s.Length - 1;

      while( i >= 0){
        while(i >= 0 && s[i] == ' '){
          i--; // if its space, skipp
        }
        int end = i;

        while(i>=0 && s[i] != ' '){
          i--;
          
        }
        int start = i + 1;
        string word = s.Substring(start, end - i);
        // start till length of word.
        words.Add(word);
      } 

      string result = string.Join(" ", words);
      Console.WriteLine(result);
      return result;
    }
}