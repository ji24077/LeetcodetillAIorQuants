public class Solution {
    public bool IsValid(string s) {
      //initialize stack
      //loops string s, 
      //if its open bracket, ->put into stack ( LIFO)
      //else: closed, 
      //peek the recent bracket and compare is it correct.

      Stack<char> stack = new Stack<char>(); //where open brackets stroe.
      foreach(char c in s){
        if(c == '(' || c == '{' || c == '['){
          stack.Push(c);
        }
        else{ // if its closed bracket.
          if(stack.Count == 0){
            return false;
          }
          char recent_open = stack.Peek();
          if( recent_open != '(' && c == ')'
          || recent_open != '[' && c == ']' || 
          recent_open != '{' &&  c == '}')
          {
            return false; //this is wrong order.

          }
          stack.Pop(); // its correct order., to endsure its fully correct.

        }
      }
      return stack.Count == 0;



    }
}