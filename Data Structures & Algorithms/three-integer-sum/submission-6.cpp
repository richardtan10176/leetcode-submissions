class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        for(int x = 0; x < nums.size(); x++){
            if(x > 0 && nums[x] == nums[x-1]){
                continue;
            }
            int conjugate = -nums[x];
            int p1 = x+1;
            int p2 = nums.size()-1;
            
            while(p1 < p2){
                if(nums[p1]+nums[p2] == conjugate){
                    ans.push_back({nums[p1], nums[p2], nums[x]});
                    p1++;
                    p2--;
                    while (p1 < p2 && nums[p1] == nums[p1 - 1]) {
                        p1++;
                    }
                    while (p1 < p2 && nums[p2] == nums[p2 + 1]) {
                        p2--;
                    }
                }
                else if(nums[p1]+nums[p2] < conjugate){
                    p1++;
                }
                else if(nums[p1]+nums[p2] > conjugate){
                    p2--;
                }
            }
        }
        return ans;
    }
};
