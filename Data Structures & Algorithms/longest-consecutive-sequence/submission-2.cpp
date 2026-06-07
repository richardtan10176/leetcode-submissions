class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()) return 0;
        unordered_map<int,int> map;
        for(int x = 0; x < nums.size(); x++){
            map[nums[x]]++;
        }
        int ans = 1;
        for(int x = 0; x < nums.size(); x++){
            int pt = nums[x]+1;
            int temp = 1;
            while(map[pt] != 0){
                temp += 1;
                pt++;
            }
            ans = max(temp, ans);
        }
        return ans;
    }
};
