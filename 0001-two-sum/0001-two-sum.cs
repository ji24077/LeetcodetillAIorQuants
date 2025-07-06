public class Solution {
    public int[] TwoSum(int[] nums, int target) {
      //create Dictionary<int,int> hmap = new Dction..
      //loops the array of nums,


     Dictionary<int, int> hmap = new Dictionary<int, int>();

     for(int i = 0; i <nums.Length; i++){
      int needed = target - nums[i]; // 9 -2 = 7
      if(hmap.ContainsKey(needed)){
        return new int[] {hmap[needed], i};
      }
      if(!hmap.ContainsKey(nums[i])){
        hmap[nums[i]] = i;
      }

     }
     return new int[] {-1,-1};
        
    }
}