public class Solution {
    public string GcdOfStrings(string str1, string str2) {
      //Substring(2) = string[2:] , Substring(i,L) = string[i: L+i].
      //L=얼마나 자를것인지. from index i.
      
      //GCD: n, m 이 있을때, n, m의 greatest common Divisor은
      // min(n.m) = n 이라고 했을떄, 
      //m % n 을 재귀저으로 나눠서 %()

      if( (str1 + str2) != (str2 + str1)){
        return ""; // 합쳐서 다르면 빈문자열.
      }
      int gcdL = GCD(str1.Length, str2.Length);
      return str1.Substring(0, gcdL);
        
    }
     private int GCD(int str1L, int str2L){
        while(str2L != 0){
          int temp = str2L; //store str2L to temp.
          str2L = str1L % str2L;
          str1L = temp;
        }
        return str1L;
      }
}