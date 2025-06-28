public class Solution {
    public IList<string> SummaryRanges(int[] nums) {
        List<string> result = new List<string>();
        int n = nums.Length;

        if (n == 0) return result; // ✅ 빈 배열 처리

        int start = nums[0]; // ✅ 구간 시작

        for (int i = 1; i < n; i++) {
            // ✅ 연속이 끊긴 지점이면, 구간 마무리
            if (nums[i] != nums[i - 1] + 1) {
                if (start == nums[i - 1]) {
                    result.Add(start.ToString()); // 예: "7"
                } else {
                    result.Add(start + "->" + nums[i - 1]); // 예: "4->6"
                }

                // ✅ 다음 구간 시작점 갱신
                start = nums[i];
            }
        }

        // ✅ 마지막 구간도 따로 처리해줘야 함
        if (start == nums[n - 1]) {
            result.Add(start.ToString());
        } else {
            result.Add(start + "->" + nums[n - 1]);
        }

        return result;
    }
}