class Solution {
public:
    int trap(vector<int>& height) {
        // 투 포인터: 양쪽 끝에서 시작
        int left = 0;
        int right = height.size() - 1;

        // 각 포인터가 지나온 최대 높이
        int leftMax = 0;
        int rightMax = 0;

        int water = 0;

        while (left < right) {

            // 왼쪽이 더 낮으면 왼쪽 처리
            // 오른쪽 최대가 더 크다고 보장되므로
            // 고이는 물 = leftMax - height[left]
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) {
                    leftMax = height[left];  // 새 최대값 갱신
                } else {
                    water += leftMax - height[left];  // 물 고임
                }
                left++;

            // 오른쪽이 더 낮으면 오른쪽 처리
            // 고이는 물 = rightMax - height[right]
            } else {
                if (height[right] >= rightMax) {
                    rightMax = height[right];  // 새 최대값 갱신
                } else {
                    water += rightMax - height[right];  // 물 고임
                }
                right--;
            }
        }

        return water;
    }
};
