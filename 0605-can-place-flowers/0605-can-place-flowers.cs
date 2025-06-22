public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
      int count = 0;
      int L = flowerbed.Length;
      for(int i = 0 ; i < L; i++){
        if(flowerbed[i] == 0){ //if current location is 0
          bool left = (i == 0 || flowerbed[i - 1] == 0); 
          bool right = (i == L - 1 || flowerbed[i + 1] == 0); // ✅ 주석과 코드 분리

          if(left && right){
            //we can plant it
            flowerbed[i] = 1;
            count++;
          }

        }

      }
      return count >= n;
        
    }
}