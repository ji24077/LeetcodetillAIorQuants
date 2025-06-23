public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        
        Dictionary<int, int> freqmap = new Dictionary<int,int>();

        foreach(int num in arr){
          if (!freqmap.ContainsKey(num)){
            freqmap[num] = 0;
          }
          freqmap[num]++;

          
        }
        HashSet<int> seen = new HashSet<int>();

        foreach( var pair in freqmap){
          int count = pair.Value;

          if(!seen.Add(count))
          {
            return false;
          }
        }
        return true;
    }
}