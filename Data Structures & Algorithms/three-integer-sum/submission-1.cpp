class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        const int n = nums.size();

        for (int i = 0; i < n; ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;     // skip duplicate first elements
            if (nums[i] > 0) break;                             // no way to sum to 0 beyond this

            int l = i + 1, r = n - 1;
            while (l < r) {
                long long s = (long long)nums[i] + nums[l] + nums[r];
                if (s < 0) {
                    ++l;
                } else if (s > 0) {
                    --r;
                } else {
                    ans.push_back({nums[i], nums[l], nums[r]});
                    ++l; --r;
                    while (l < r && nums[l] == nums[l - 1]) ++l; // skip duplicate seconds
                    while (l < r && nums[r] == nums[r + 1]) --r; // skip duplicate thirds
                }
            }
        }
        return ans;
    }
};
