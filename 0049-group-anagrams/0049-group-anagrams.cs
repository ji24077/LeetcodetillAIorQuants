public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        
      Dictionary<string, List<string>> hmap = new Dictionary<string, List<string>>();

      // { aet :  [eat, tea, ..]}

      foreach(string word in strs){
        char[] charArr = word.ToCharArray(); // to sort.

        Array.Sort(charArr); // this is for key

        string key = new string(charArr);

        if(!hmap.ContainsKey(key)){
          hmap[key] = new List<string>();
        }
        hmap[key].Add(word);//여기서, key는 항상 같음, 아나그램이면, 정렬하기땨문.
      }
      return new List<IList<string>>(hmap.Values);



    }
}