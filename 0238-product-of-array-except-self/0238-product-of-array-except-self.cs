public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] answer = new int[n];

        // ✅ Step 1: 왼쪽 누적곱 계산
        answer[0] = 1;  // 왼쪽에 곱할 게 없으므로 1
        for (int i = 1; i < n; i++) {
            answer[i] = answer[i - 1] * nums[i - 1];
        }

        // ✅ Step 2: 오른쪽 누적곱과 곱하기
        int right = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }

        return answer;
    }
}