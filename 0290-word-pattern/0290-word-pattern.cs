public class Solution{
  public bool WordPattern(string pattern, string s){
    string[] words = s.Split(' '); //[dog, cat, cat, dog]

  //two map: Dictionary<char, string> hmap1, Dictionary<string, char> hmap2;

  //for i< pattern.Length : char p = pattern[i], string word = words[i]
  //just compare map1.ContainsKey() ,ow mapping, similary for map2.

  Dictionary<char,string> mapPWord = new Dictionary<char, string>();

  Dictionary<string,char> mapWordP = new Dictionary<string, char>();
  if(pattern.Length != words.Length){
    return false;
  }

  for(int i =0; i < pattern.Length; i++){
      char p = pattern[i];
      string word = words[i];
      if(mapPWord.ContainsKey(p)){
        if(mapPWord[p] != word){
          return false;
        }
      }
      else{
        mapPWord[p] = word;
      }
      if(mapWordP.ContainsKey(word)){
        if(mapWordP[word] != p){
          return false;
        }
      }
      else{
        mapWordP[word] = p;
      }
    }
    return true;
  }
}