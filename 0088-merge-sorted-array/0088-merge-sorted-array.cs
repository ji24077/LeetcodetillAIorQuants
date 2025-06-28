public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
      int k = m + n -1;
      int right = m - 1;
      int left = n - 1;
      while(left >= 0){
        if(right >= 0 && nums1[right] > nums2[left]){
          nums1[k--] = nums1[right--];
         
        }
        else{
          nums1[k--] = nums2[left--];
          
        }
       

      }
    }
}