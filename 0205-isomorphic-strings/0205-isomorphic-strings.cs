public class Solution {
    public bool IsIsomorphic(string s, string t) {
      Dictionary<char, char> MapST = new Dictionary<char, char>();
      Dictionary<char, char> MapTS = new Dictionary<char, char>();
      //givem all s, t are has same length.
      for (int i = 0; i < s.Length; i++){
        char cs = s[i];
        char ct = t[i];

        if( MapST.ContainsKey(cs)){
          if (MapST[cs] != ct){
            return false;

          }
         
        }
         else{
            MapST[cs] = ct;
          }
        if ( MapTS.ContainsKey(ct)){
          if ( MapTS[ct] != cs){
            return false;
          }
         
        }
         else{
            MapTS[ct] = cs;
          }

      }
      return true;

        
    }
}