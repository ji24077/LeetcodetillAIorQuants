public class Solution {
    public int HIndex(int[] citations) {
      Array.Sort(citations);

      int n = citations.Length;
      //[0,1,3,5,6] after sorted.
      //so, now, what is h? after sorted.-> n-i bc remained reserach paper.


      for( int i = 0; i < n; i++){
        int h = n - i;
        if(citations[i] >= h){ // since its sorted, when this conditon meets, #hth.
          // #h paper's cited at lest #h times. sorted
          return h;
        }


      }
      return 0;
        
    }
}