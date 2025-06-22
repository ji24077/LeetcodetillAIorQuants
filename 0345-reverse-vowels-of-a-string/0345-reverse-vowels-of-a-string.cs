public class Solution {
    public string ReverseVowels(string s) {
      HashSet<char> vowels = new HashSet<char>(){
        'a', 'e', 'i','o','u', 'A', 'E', 'I', 'O', 'U'
      };
      int left = 0;
      int right = s.Length - 1;
      char[] chars = s.ToCharArray();
      while( left < right){
        //while left and right are diff.
        while(left < right && !vowels.Contains(chars[left])){
          //then here we have left index with non vowels.
          //then we loop
          left++;

        }
        while(left < right && !vowels.Contains(chars[right])){
          //
          right--;
        }
        char temp = chars[left];
        chars[left] = chars[right];
        chars[right] = temp;
        left++;
        right--;


      }
      return new string(chars);
        
    }
}