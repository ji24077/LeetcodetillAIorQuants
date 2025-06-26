public class Solution {
    public string RemoveStars(string s) {
      Stack<char> stack = new Stack<char>();
      
      foreach (char chr in s){
        if( chr != '*'){
          stack.Push(chr);
        }
        else{// if chr == '*
          stack.Pop();
        }

      }
      char[] result = stack.Reverse().ToArray();
      return new string(result);

        
    }
}