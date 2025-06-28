public class Solution {
    public bool CanConstruct(string ransomNote, string magazine) {

      Dictionary< char, int> Hashmap = new Dictionary<char, int>();
      // char : key

      //first i am going to store num of each char in magazine, ie) char : count

      foreach(char c in magazine){
        if(!Hashmap.ContainsKey(c)){
          Hashmap[c] = 0;
        }
        Hashmap[c]++;
      }
      
      //now it has key and num of magazine's char

      foreach(char c in ransomNote){
        if(!Hashmap.ContainsKey(c) || Hashmap[c] == 0){
          return false;
        }
        Hashmap[c]--;
      }
      return true;
        
    }
}