public class Solution {
    public int Jump(int[] nums) {
        
        int count = 0; // count if jump.
        int jumpPossible = 0; // how far u can jump at ith.
        int end_jump = 0; //end index at this ith jump
        for( int i = 0; i < nums.Length - 1; i++){// 마지막 인덱스는 점프않해도됨.
          jumpPossible = Math.Max(jumpPossible, i + nums[i]);

          if(i == end_jump){
            count++;
            end_jump = jumpPossible;

          }

        }
        return count;
    }
}