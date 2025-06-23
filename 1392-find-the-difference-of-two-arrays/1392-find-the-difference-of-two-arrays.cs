public class Solution {
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
      //recall: set( Hashset)은 증복을 없에줌.
      HashSet<int> set1 = new HashSet<int>(nums1);
      HashSet<int> set2 = new HashSet<int>(nums2);

      List<int> onlyInnums1 = new List<int>();
      foreach(int num in set1){
        if(!set2.Contains(num)){
          //if not in set2, add into onlyInnums1.
          onlyInnums1.Add(num);
        }

      }
      List<int> onlyInnums2 = new List<int>();
      foreach(int num in set2){
        if(!set1.Contains(num)){
          onlyInnums2.Add(num);
        }
      }
      return new List<IList<int>>(){onlyInnums1,onlyInnums2};
        
    }
}