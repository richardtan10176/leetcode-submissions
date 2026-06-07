class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<pair<int,int>> v;
        unordered_map<int,int> map;
        for(int x = 0; x < nums.size(); x++){
            map[nums[x]]++;
        }
        for(auto& it: map){
            pair<int,int> p(it.second,it.first);
            v.push_back(p);
        }
        sort(v.rbegin(), v.rend());
        vector<int> ans;
        for(int x = 0; x < k; x++){
            ans.push_back(v[x].second);
        }

        return ans;
    }
};
