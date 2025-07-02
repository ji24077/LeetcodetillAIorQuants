public class Solution {
    public string SimplifyPath(string path) {
        // /a/./b/.../c/-> /c
        //Stack<string> stack for storig path.
        //string[] parts = path.Split('/'); ["","a",..]
        //foreach(string str in path){}
        Stack<string> stack = new Stack<string>();

        string[] parts = path.Split('/');   

        foreach(string part in parts){
          if( part == "." || part == ""){
            continue;
          }
          else if(part == ".."){
            if(stack.Count>0){
                 stack.Pop(); //remove prev parent

            }    
          }
          else{
            //valid, just add on path.
            stack.Push(part);
          }
        } 
        var result = "/" + string.Join("/", stack.Reverse());
        return result;
    }
}