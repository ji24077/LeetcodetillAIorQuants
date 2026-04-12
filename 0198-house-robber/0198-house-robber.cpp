class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty()){
          return 0;
        }
        int prev2 = 0;
        int prev1 = 0;
        for (int i = 0; i < nums.size(); i++)
        {
          int take = prev2 + nums[i];
          int skip = prev1;
          int current = max(take, skip);

          prev2 = prev1;
          prev1 = current;


        }
        int result = prev1;

        return result;
    }
};