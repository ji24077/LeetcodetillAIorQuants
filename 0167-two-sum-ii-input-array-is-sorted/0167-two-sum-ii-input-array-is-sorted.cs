public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
      //
      // for(int i = 0; i < numbers.Length; i++){
      //   for(int j = i + 1; j < numbers.Length; j++){
      //     if(numbers[i] + numbers[j] == target){
      //       return new int[] { i+1, j+1};
      //     }
      //   }
      // }
      // return new int
      

      //starting from left = 0;
      // int right = numbers.Length -1;
      //idea: when you loops while left < right:
      //->  sum = nums[left]+ nums[right]
      //if sum < target->left++ similary for right, if its sum == target-> [indexes+1]

      int left = 0;
      int right = numbers.Length -1;
      while (left < right){
        int sum = numbers[left] + numbers[right];
        if(sum == target){
          return new int[] {left+1, right+1};
        }
        else if(sum < target){
          left++;
        }
        else{
          right--;
        }
      }
      return new int[] {-1, -1};
    }
}