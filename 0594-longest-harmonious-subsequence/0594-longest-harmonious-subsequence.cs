public class Solution {
    public int FindLHS(int[] nums) {
        Dictionary<int,int> hmap = new Dictionary<int,int>();

        foreach(int num in nums){
          if(!hmap.ContainsKey(num))
          {
            hmap[num] = 0;
          }
          hmap[num]++;
        }
        //1 :1, 3: 2, 2: 3,..
        //hmap[1], hmap[2] = 
        int result = 0;

        foreach(int key in hmap.Keys){
          
          if(hmap.ContainsKey(key +1)){
            int len = hmap[key] + hmap[key + 1];
            result = Math.Max(len, result);

          }
        }
        return result;


    }
}