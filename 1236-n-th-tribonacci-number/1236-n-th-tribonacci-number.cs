public class Solution {
    public int Tribonacci(int n) {
      if(n == 0){
        return 0;
      }
      if( n == 1 || n == 2){
        return 1;
      }
      //Tn+3 = Tn + Tn+1 + Tn+2, n >=0, 
      // <=> Tn = Tn-3 + Tn-2 + Tn-1
      int t0 = 0;
      int t1 = 1;
      int t2 = 1; // these are dps.
      for( int i = 3; i <= n; i++){
        int  t3 = t0 + t1 + t2;
        t0 = t1;
        t1 = t2;
        t2 = t3; //most recent value tn-1
      }
      return t2;

    }
}