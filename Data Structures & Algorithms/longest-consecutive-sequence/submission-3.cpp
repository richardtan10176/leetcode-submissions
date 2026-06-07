class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;

        unordered_set<int> set(nums.begin(), nums.end());
        int ans = 0;

        for (int num : set) {
            if (!set.count(num - 1)) {
                int current = num;
                int streak = 1;

                while (set.count(current + 1)) {
                    current++;
                    streak++;
                }

                ans = max(ans, streak);
            }
        }

        return ans;
    }
};
