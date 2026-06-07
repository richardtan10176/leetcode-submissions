class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans;
        for(int x = 0; x < nums.size(); x++){
            int num = 1;
            for(int i = 0; i < nums.size(); i++){
                if(i == x) continue;
                num *= nums[i];
            }
            ans.push_back(num);
        }
        return ans;
    }
};
